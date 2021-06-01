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
#ifndef BIT_H
#define BIT_H


#include "libgpdwg.h"



void bit_advance_position (Bit_Data *dat, int16_t advance);
BITCODE_B bit_read_B (Bit_Data * dat);
BITCODE_BB bit_read_BB (Bit_Data * dat);
BITCODE_BD bit_read_BD (Bit_Data * dat);
BITCODE_BD3 bit_read_BD3 (Bit_Data * dat);
BITCODE_BL bit_read_BL (Bit_Data * dat);
BITCODE_BLL bit_read_BLL (Bit_Data * dat);
BITCODE_BS bit_read_BS (Bit_Data * dat);
BITCODE_CMC bit_read_CMC (Bit_Data * dat);
BITCODE_H bit_read_H (Bit_Data * dat);
BITCODE_RC bit_read_RC (Bit_Data * dat);
BITCODE_RD bit_read_RD (Bit_Data * dat);
BITCODE_RD2 bit_read_RD2 (Bit_Data *dat);
BITCODE_RL bit_read_RL (Bit_Data * dat);
BITCODE_T bit_read_T (Bit_Data *dat);
BITCODE_TV bit_read_TV (Bit_Data *dat);

BITCODE_RS bit_read_RS (Bit_Data * dat);

uint16_t bit_crc8 (uint16_t dx, uint8_t * adr, uint32_t n, uint32_t y);
unsigned char * decode_sentinel (DWG_SENTINAL s);
int check_sentinal (Bit_Data  *dat, unsigned char *sentinal);




BITCODES_ALL readwithlog(BITCODE_TYPE t, Bit_Data *dat, char *comment);


#endif