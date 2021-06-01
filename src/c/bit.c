/*****************************************************************************/
/*  libgpdwg - free c library to read .dwg files.                               */
/*                                                                           */
/*  Copyright (C) 2018-2021 Guruprasad Rane <raneguruprasad@gmail.com>       */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License version 3. You should have received a copy of     */
/*  the GNU General Public License along with this program.                  */
/*                                                                           */
/*****************************************************************************/
#include "bit.h"
#include "logger.h"
#include "libgpdwg.h"
#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>






/** Advance bits (forward or backward) */
void bit_advance_position (Bit_Data *dat, int16_t advance)
{
  int endpos;

  endpos = dat->bit + advance;
  if (dat->byte >= dat->size - 1 && endpos > 7)
    {
      dat->bit = 7;
      return;
    }
  dat->bit = endpos % 8;
  dat->byte += endpos / 8;
}

/** Read 1 bit */
BITCODE_B bit_read_B (Bit_Data * dat)
{
  uint8_t result;
  uint8_t byte;

  byte = dat->chain[dat->byte];
  result = (byte & (0x80 >> dat->bit)) >> (7 - dat->bit);

  bit_advance_position (dat, 1);
  return result;
}

/** Read 2 bits */
BITCODE_BB bit_read_BB (Bit_Data * dat)
{
  uint8_t result;
  uint8_t byte;

  byte = dat->chain[dat->byte];
  if (dat->bit < 7)
    result = (byte & (0xc0 >> dat->bit)) >> (6 - dat->bit);
  else
    {
      result = (byte & 0x01) << 1;
      if (dat->byte < dat->size - 1)
  {
    byte = dat->chain[dat->byte + 1];
    result |= (byte & 0x80) >> 7;
  }
    }

  bit_advance_position (dat, 2);
  return result;
}

/** Read 1 bitdouble (compacted data) */
BITCODE_BD bit_read_BD (Bit_Data * dat)
{
  uint8_t two_bit_code;
  int32_t *res;
  double result;

  two_bit_code = bit_read_BB (dat);

  if (two_bit_code == 0)
    {
      result = bit_read_RD (dat);
      return (result);
    }
  else if (two_bit_code == 1)
    return (1.0);
  else if (two_bit_code == 2)
    return (0.0);
  else        /* if (two_bit_code == 3) */
    {
      fprintf(stderr,"bit_read_BD: unexpected 2-bit code: '11'\n");
      /* create a Not-A-Number (NaN) */
      res = (int32_t *) &result;
      res[0] = -1;
      res[1] = -1;
      return (result);
    }
}

/* Read point 3BD */
BITCODE_BD3 bit_read_BD3 (Bit_Data * dat)
{
  BITCODE_BD3 result;
  result.x=bit_read_BD(dat);
  result.y=bit_read_BD(dat);
  result.z=bit_read_BD(dat);
  return result;
}

BITCODE_BL bit_read_BL (Bit_Data * dat)
{
  uint8_t two_bit_code;
  uint32_t result;

  two_bit_code = bit_read_BB (dat);

  if (two_bit_code == 0)
    {
      result = bit_read_RL (dat);
      return (result);
    }
  else if (two_bit_code == 1)
    {
      result = bit_read_RC (dat) & 0xFF;
      return (result);
    }
  else if (two_bit_code == 2)
    return (0);
  else
    /* if (two_bit_code == 3) */
    {
      fprintf (stderr,"bit_read_BL: unexpected 2-bit code: '11'\n");
      return (256);
    }
}

BITCODE_BLL bit_read_BLL (Bit_Data * dat)
{
  fprintf (stderr,"ERROR - BLL function need to be worked out.");
}

/** Read 1 bitshort (compacted data) */
BITCODE_BS bit_read_BS (Bit_Data * dat)
{
  uint8_t two_bit_code;
  uint16_t result;

  two_bit_code = bit_read_BB (dat);

  if (two_bit_code == 0)
    {
      result = bit_read_RS (dat);
      return (result);
    }
  else if (two_bit_code == 1)
    {
      result = (uint8_t) bit_read_RC (dat);
      return (result);
    }
  else if (two_bit_code == 2)
    return (0);
  else
    /* if (two_bit_code == 3) */
    return (256);
}
/*
# Read Color
def read_CMC(dat):
  result=color()
  result.index=read_BS(dat)
  result.name=""
  result.book_name=""
  if dat.version >= 2004:
    result.rgb = read_BL(dat)
    result.byte = read_RC(dat)
    if result.byte & 1:
      result.name = read_TV(dat)
    if result.byte & 2:
      result.book_name = read_TV(dat)
  return result
  */


/** Read color */
BITCODE_CMC bit_read_CMC (Bit_Data * dat)
{
  BITCODE_CMC color;
  color.index = bit_read_BS (dat);
  color.name = "";
  color.book_name = "";
  if (dat->version >= 2004)
    {
      color.rgb = bit_read_BL (dat);
      color.byte = bit_read_RC (dat);
      if (color.byte & 1)
  color.name = (char *) bit_read_TV (dat);
      if (color.byte & 2)
  color.book_name = (char *) bit_read_TV (dat);
    }
  return color;
}

/** Read handle-references */
BITCODE_H bit_read_H (Bit_Data * dat)
{
  BITCODE_H handle;
  uint8_t val;
  uint8_t i;

  handle.code = bit_read_RC (dat);
  handle.size = handle.code & 0x0f;
  handle.code = (handle.code) >> 4;

  for (int i = 0; i < handle.size; ++i)
  {
    val=(val << 8) + bit_read_RC (dat);
  }
  handle.value = val;
  return handle;
}
/** Read 1 byte (raw char) */
BITCODE_RC bit_read_RC (Bit_Data *dat)
{
  uint8_t result;
  uint8_t byte;

  byte = dat->chain[dat->byte];
  if (dat->bit == 0)
    result = byte;
  else
    {
      result = byte << dat->bit;
      if (dat->byte < dat->size - 1)
  {
    byte = dat->chain[dat->byte + 1];
    result |= byte >> (8 - dat->bit);
  }
    }

  bit_advance_position (dat, 8);
  return ((uint8_t) result);
}

/** Read 1 raw double (8 bytes) */
BITCODE_RD bit_read_RD (Bit_Data * dat)
{
  int i;
  uint8_t byte[8];
  double *result;

  //TODO: I think it might not work on big-endian platforms
  for (i = 0; i < 8; i++)
    byte[i] = bit_read_RC (dat);

  result = (double *) byte;
  return (*result);
}

BITCODE_RD2 bit_read_RD2 (Bit_Data *dat)
{
  BITCODE_RD2 result;
  result.x=bit_read_RD(dat);
  result.y=bit_read_RD(dat);
  return result;
}
/** Read 1 raw long (2 words) */
BITCODE_RL bit_read_RL (Bit_Data * dat)
{
  uint16_t word1, word2;

  // least significant word first
  word1 = bit_read_RS (dat);
  word2 = bit_read_RS (dat);
  return ((((uint32_t) word2) << 16) | ((uint32_t) word1));
}

BITCODE_T bit_read_T (Bit_Data *dat)
{
  return bit_read_TV (dat);
}

BITCODE_TV bit_read_TV (Bit_Data *dat)
{
  uint16_t i;
  uint16_t length;
  uint8_t *chain;

  length = bit_read_BS (dat);
  if (length > 5000)
    return (NULL);
  chain = (uint8_t *) malloc (length + 64);
  for (i = 0; i < length; i++)
    {
      chain[i] = bit_read_RC (dat);
      if ((chain[i]) == '\0')
        break;
      else if ((chain[i]) == '\n')
      {
        chain[i] = '^';
  i++;
        chain[i] = 'J';
  length++;
      }
      else if (!isprint (chain[i]))
      {
        if (length > 0)
  {
    i--;
    length--;
  }
  else
    break;
      }
    }
  chain[i] = '\0';

  return (chain);
}





/** Read 1 word (raw short) */
BITCODE_RS bit_read_RS (Bit_Data *dat)
{
  uint8_t byte1, byte2;

  // least significant byte first
  byte1 = bit_read_RC (dat);
  byte2 = bit_read_RC (dat);
  return ((uint16_t) ((byte2 << 8) | byte1));
}



BITCODES_ALL readwithlog(BITCODE_TYPE t, Bit_Data *dat, char *comment)
{
  BITCODES_ALL output;
  fprintf(stderr,"DEBUG: %i - %i %s - ", dat->byte, dat->bit, comment);
  switch (t){
    case B:
      output.bitcode_b=bit_read_B(dat);
      fprintf(stderr, "%" FORMAT_B "\n", output.bitcode_b);
      break;
    case BD:
      output.bitcode_bd=bit_read_BD(dat);
      fprintf(stderr, "%" FORMAT_BD "\n", output.bitcode_bd);
      break;
    case BD3:
      output.bitcode_bd3=bit_read_BD3(dat);
      fprintf(stderr, "Point2D(%"PRIu16",%"PRIu16",%"PRIu16")\n", output.bitcode_bd3.x,  output.bitcode_bd3.y,  output.bitcode_bd3.z );
      break;
    case BL:
      output.bitcode_bl=bit_read_BL(dat);
      fprintf(stderr, "%" FORMAT_BL "\n", output.bitcode_bl);
      break;
    case BLL:
      output.bitcode_bll=bit_read_BLL(dat);
      fprintf(stderr, "%" FORMAT_BLL "\n", output.bitcode_bll);
      break;
    case BS:
      output.bitcode_bs=bit_read_BS(dat);
      fprintf(stderr, "%" FORMAT_BS "\n", output.bitcode_bs);
      break;
    case CMC:
      output.bitcode_cmc=bit_read_CMC(dat);
      fprintf(stderr, "Color(%s,%i,%i,%s,%i)\n", output.bitcode_cmc.book_name,  output.bitcode_cmc.index,  output.bitcode_cmc.byte,  output.bitcode_cmc.name,  output.bitcode_cmc.rgb );
      break;
    case H:
      output.bitcode_h=bit_read_H(dat);
      fprintf(stderr, "Handle(%i,%i,%i)\n", output.bitcode_h.code,  output.bitcode_h.size,  output.bitcode_h.value );
      break;
    case RC:
      output.bitcode_rc=bit_read_RC(dat);
      fprintf(stderr, "%" FORMAT_RC "\n", output.bitcode_rc);
      break;
    case RD2:
      output.bitcode_rd2=bit_read_RD2(dat);
      fprintf(stderr, "Point(%"PRIu16",%"PRIu16")\n", output.bitcode_rd2.x,  output.bitcode_rd2.y );
      break;
    case RL:
      output.bitcode_rl=bit_read_RL(dat);
      fprintf(stderr, "%" FORMAT_RL "\n", output.bitcode_rl);
      break;
    case RS:
      output.bitcode_rs=bit_read_RS(dat);
      fprintf(stderr, "%" FORMAT_RS "\n", output.bitcode_rs);
      break;
    case T:
      output.bitcode_t=bit_read_T(dat);
      fprintf(stderr, "%s\n", output.bitcode_t);
      break;
    case TV:
      output.bitcode_tv=bit_read_TV(dat);
      fprintf(stderr, "%s\n", output.bitcode_tv);
      break;

  }
  return output;
}


/*
BITCODES_ALL readwithlog(BITCODE_TYPE t, Bit_Data *dat, char *comment)
{
	BITCODES_ALL output;
	fprintf(stderr,"DEBUG: %i - %i %s - ", dat->byte, dat->bit, comment);
	switch (t){
		case RC:
			output.bitcode_rc=bit_read_RC(dat);
			fprintf(stderr, FORMAT_RC "\n", output.bitcode_rc);
			break;
    case MC:
      output.bitcode_rc=bit_read_MC(dat);
      fprintf(stderr, "%" FORMAT_MC "\n", output.bitcode_mc);
      break;
    case MS:
      output.bitcode_ms=bit_read_MS(dat);
      fprintf(stderr, "%" FORMAT_MS "\n", output.bitcode_ms);
      break;
    case B:
      output.bitcode_b=bit_read_B(dat);
      fprintf(stderr, "%" FORMAT_B "\n", output.bitcode_b);
      break;
    case BB:
      output.bitcode_bb=bit_read_BB(dat);
      fprintf(stderr, "%" FORMAT_BB "\n", output.bitcode_bb);
      break;


		case RL:
			output.bitcode_rl=bit_read_RL(dat);
			fprintf(stderr, "%" FORMAT_RL "\n", output.bitcode_rl);
			break;
    case RS:
      output.bitcode_rs=bit_read_RS(dat);
      fprintf(stderr, "%" FORMAT_RS "\n", output.bitcode_rs);
      break;
	}
	return output;
}
*/

/*
  BITCODE_RC bitcode_rc;
  BITCODE_MC bitcode_mc;
  BITCODE_MS bitcode_ms;
  BITCODE_B  bitcode_b;
  BITCODE_BB bitcode_bb;
  BITCODE_BS bitcode_bs;
  BITCODE_RS bitcode_rs;
  BITCODE_RL bitcode_rl;
  BITCODE_RD bitcode_rd;
  BITCODE_BL bitcode_bl;
  BITCODE_TV bitcode_tv;
  BITCODE_BT bitcode_bt;
  BITCODE_DD bitcode_dd;
  BITCODE_BD bitcode_bd;
  BITCODE_BE bitcode_be;
  BITCODE_H  bitcode_h;
  BITCODE_T  bitcode_t;
*/



/** 8-bit CRC */
uint16_t bit_crc8 (uint16_t dx, uint8_t * adr, uint32_t n, uint32_t y)
{
  int StartByte=y;
  int NoOfSteps=n;
  register uint16_t al;
  uint8_t intadr;
  static uint16_t ckrtable[256] =
    { 0x0000, 0xC0C1, 0xC181, 0x0140, 0xC301, 0x03C0, 0x0280, 0xC241, 0xC601,
    0x06C0, 0x0780, 0xC741, 0x0500, 0xC5C1, 0xC481, 0x0440, 0xCC01, 0x0CC0,
    0x0D80, 0xCD41, 0x0F00, 0xCFC1, 0xCE81, 0x0E40, 0x0A00, 0xCAC1, 0xCB81,
    0x0B40, 0xC901, 0x09C0, 0x0880, 0xC841, 0xD801, 0x18C0, 0x1980, 0xD941,
    0x1B00, 0xDBC1, 0xDA81, 0x1A40, 0x1E00, 0xDEC1, 0xDF81, 0x1F40, 0xDD01,
    0x1DC0, 0x1C80, 0xDC41, 0x1400, 0xD4C1, 0xD581, 0x1540, 0xD701, 0x17C0,
    0x1680, 0xD641, 0xD201, 0x12C0, 0x1380, 0xD341, 0x1100, 0xD1C1, 0xD081,
    0x1040, 0xF001, 0x30C0, 0x3180, 0xF141, 0x3300, 0xF3C1, 0xF281, 0x3240,
    0x3600, 0xF6C1, 0xF781, 0x3740, 0xF501, 0x35C0, 0x3480, 0xF441, 0x3C00,
    0xFCC1, 0xFD81, 0x3D40, 0xFF01, 0x3FC0, 0x3E80, 0xFE41, 0xFA01, 0x3AC0,
    0x3B80, 0xFB41, 0x3900, 0xF9C1, 0xF881, 0x3840, 0x2800, 0xE8C1, 0xE981,
    0x2940, 0xEB01, 0x2BC0, 0x2A80, 0xEA41, 0xEE01, 0x2EC0, 0x2F80, 0xEF41,
    0x2D00, 0xEDC1, 0xEC81, 0x2C40, 0xE401, 0x24C0, 0x2580, 0xE541, 0x2700,
    0xE7C1, 0xE681, 0x2640, 0x2200, 0xE2C1, 0xE381, 0x2340, 0xE101, 0x21C0,
    0x2080, 0xE041, 0xA001, 0x60C0, 0x6180, 0xA141, 0x6300, 0xA3C1, 0xA281,
    0x6240, 0x6600, 0xA6C1, 0xA781, 0x6740, 0xA501, 0x65C0, 0x6480, 0xA441,
    0x6C00, 0xACC1, 0xAD81, 0x6D40, 0xAF01, 0x6FC0, 0x6E80, 0xAE41, 0xAA01,
    0x6AC0, 0x6B80, 0xAB41, 0x6900, 0xA9C1, 0xA881, 0x6840, 0x7800, 0xB8C1,
    0xB981, 0x7940, 0xBB01, 0x7BC0, 0x7A80, 0xBA41, 0xBE01, 0x7EC0, 0x7F80,
    0xBF41, 0x7D00, 0xBDC1, 0xBC81, 0x7C40, 0xB401, 0x74C0, 0x7580, 0xB541,
    0x7700, 0xB7C1, 0xB681, 0x7640, 0x7200, 0xB2C1, 0xB381, 0x7340, 0xB101,
    0x71C0, 0x7080, 0xB041, 0x5000, 0x90C1, 0x9181, 0x5140, 0x9301, 0x53C0,
    0x5280, 0x9241, 0x9601, 0x56C0, 0x5780, 0x9741, 0x5500, 0x95C1, 0x9481,
    0x5440, 0x9C01, 0x5CC0, 0x5D80, 0x9D41, 0x5F00, 0x9FC1, 0x9E81, 0x5E40,
    0x5A00, 0x9AC1, 0x9B81, 0x5B40, 0x9901, 0x59C0, 0x5880, 0x9841, 0x8801,
    0x48C0, 0x4980, 0x8941, 0x4B00, 0x8BC1, 0x8A81, 0x4A40, 0x4E00, 0x8EC1,
    0x8F81, 0x4F40, 0x8D01, 0x4DC0, 0x4C80, 0x8C41, 0x4400, 0x84C1, 0x8581,
    0x4540, 0x8701, 0x47C0, 0x4680, 0x8641, 0x8201, 0x42C0, 0x4380, 0x8341,
    0x4100, 0x81C1, 0x8081, 0x4040
  };
  while (n > 0)
  {
    intadr = adr[y];
    al = intadr ^ (dx & 255);
    dx = (dx >> 8) & 255;
    dx = dx ^ ckrtable[al & 255];
    y = y + 1;
    n = n - 1;
  }
  printf("DEBUG - Reading CRC from %" PRIu32 " for %" PRIu32" bytes = %"PRIu16"\n", StartByte, NoOfSteps, dx);
  return (dx);
}

unsigned char * decode_sentinel (DWG_SENTINAL s)
{
  static unsigned char sentinels[9][16] = {
    {0x95, 0xA0, 0x4E, 0x28, 0x99, 0x82, 0x1A, 0xE5, 0x5E, 0x41, 0xE0, 0x5F,
     0x9D, 0x3A, 0x4D, 0x00},
    {0x1F, 0x25, 0x6D, 0x07, 0xD4, 0x36, 0x28, 0x28, 0x9D, 0x57, 0xCA, 0x3F,
     0x9D, 0x44, 0x10, 0x2B},
    {0xE0, 0xDA, 0x92, 0xF8, 0x2B, 0xc9, 0xD7, 0xD7, 0x62, 0xA8, 0x35, 0xC0,
     0x62, 0xBB, 0xEF, 0xD4},
    {0xCF, 0x7B, 0x1F, 0x23, 0xFD, 0xDE, 0x38, 0xA9, 0x5F, 0x7C, 0x68, 0xB8,
     0x4E, 0x6D, 0x33, 0x5F},
    {0x30, 0x84, 0xE0, 0xDC, 0x02, 0x21, 0xC7, 0x56, 0xA0, 0x83, 0x97, 0x47,
     0xB1, 0x92, 0xCC, 0xA0},
    {0x8D, 0xA1, 0xC4, 0xB8, 0xC4, 0xA9, 0xF8, 0xC5, 0xC0, 0xDC, 0xF4, 0x5F,
     0xE7, 0xCF, 0xB6, 0x8A},
    {0x72, 0x5E, 0x3B, 0x47, 0x3B, 0x56, 0x07, 0x3A, 0x3F, 0x23, 0x0B, 0xA0,
     0x18, 0x30, 0x49, 0x75},
    {0xD4, 0x7B, 0x21, 0xCE, 0x28, 0x93, 0x9F, 0xBF, 0x53, 0x24, 0x40, 0x09,
     0x12, 0x3C, 0xAA, 0x01},
    {0x2B, 0x84, 0xDE, 0x31, 0xD7, 0x6C, 0x60, 0x40, 0xAC, 0xDB, 0xBF, 0xF6,
     0xED, 0xC3, 0x55, 0xFE}
  };

  return (sentinels[s]);
}

int check_sentinal (Bit_Data  *dat, unsigned char *sentinal)
{
  for (int i = 0; i < 16; ++i)
  {
    if(bit_read_RC(dat) != sentinal[i])
    {
      logger(LOG_ERROR,dat->byte,dat->bit,"Sentinal not found.");
      return -1;
    }
  }
  logger(LOG_INFO,dat->byte,dat->bit,"Sentinal found at correct location.");
  return 0;
}





/*
def check_Sentinel(dat,sentinel):
  for j in range (0,16):
    StartPos=dat.byte
    #if readwithlog("RC",dat,"Sentinel "+str(j),1) != int(sentinel[j],16):
    if read_RC(dat) != int(sentinel[j],16):
      logger.error( str(StartPos) + " Sentinel not found at correct location.")
      return False
  logger.info("Sentinel found at correct location.")
  return True
*/