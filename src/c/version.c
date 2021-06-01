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
#include "version.h"
#include "variables.h"
#include "bit.h"
#include <stdio.h>
#include <inttypes.h>
#include <stddef.h>
#include <stdlib.h>


uint32_t get_section_address(int number, Gpdwg_Data *gpdwg)
{
	int count = gpdwg->header.sectionCount;
	Gpdwg_Section *Section_cur = gpdwg->header.section;
	Gpdwg_Section *Section_next = NULL;
	while(number != Section_cur->number)
	{
		Section_next = Section_cur->next;
		Section_cur = Section_next;
	}
	return Section_cur->address;
}

uint32_t get_section_size(int number, Gpdwg_Data *gpdwg)
{
	int count = gpdwg->header.sectionCount;
	Gpdwg_Section *Section_cur = gpdwg->header.section;
	Gpdwg_Section *Section_next = NULL;
	while(number != Section_cur->number)
	{
		Section_next = Section_cur->next;
		Section_cur = Section_next;
	}
	return Section_cur->size;
}

int decode_2000(Bit_Data *dat, Gpdwg_Data *gpdwg)
{
	BITCODES_ALL read_data;
	BITCODE_RS crc1;
	BITCODE_RS crc2;
	dat->version=2000;
	logger(LOG_DEBUG,dat->byte,dat->bit,"Starting to decode version 2000 file.");
	dat->byte=19;
	read_data=readwithlog(RC,dat,"Codepage"); gpdwg->header.codepage=read_data.bitcode_rc;
	dat->byte=21; dat->bit=0;
	read_data=readwithlog(RL,dat,"Section Count"); gpdwg->header.sectionCount=read_data.bitcode_rl;
	logger(LOG_DEBUG,dat->byte,dat->bit,"Reading section count done.");
	Gpdwg_Section *Last_Handle = NULL;
	
	for (int i = 0; i < gpdwg->header.sectionCount; ++i)
	{
		Gpdwg_Section *Temp_Section;
		Temp_Section = malloc(sizeof(Gpdwg_Section));
		read_data = readwithlog(RC,dat,"Section Number");
		Temp_Section->number = read_data.bitcode_rc;
		read_data = readwithlog(RL,dat,"Section Address");
		Temp_Section->address = read_data.bitcode_rl;
		read_data = readwithlog(RL,dat,"Section Size");
		Temp_Section->size = read_data.bitcode_rl;
		Temp_Section->next = Last_Handle;
		Last_Handle = Temp_Section;
	}
	gpdwg->header.section = Last_Handle;
	logger(LOG_DEBUG,dat->byte,dat->bit,"Reading section details done.");
	crc1 = bit_crc8(0xc0c1,dat->chain,dat->byte,0);
	read_data = readwithlog(RS,dat,"CRC2"); crc2=read_data.bitcode_rs;
	if(crc1 == crc2)
	{
		logger(LOG_INFO,dat->byte,dat->bit,"CRC match.");
	}else{
		logger(LOG_ERROR,dat->byte,dat->bit,"CRC mismatch.");
	}
	logger(LOG_INFO,dat->byte,dat->bit,"Checking Header Sentinal.");
	check_sentinal(dat,decode_sentinel(DWG_SENTINEL_HEADER_END));

// decode Variables.
	logger(LOG_INFO,dat->byte,dat->bit,"Starting to decode variables.");
	dat->byte=get_section_address(0,gpdwg);
	dat->bit=0;
	logger(LOG_INFO,dat->byte,dat->bit,"Starting to read section no 0.");
	check_sentinal(dat,decode_sentinel(DWG_SENTINEL_VARIABLE_BEGIN));
	readwithlog(RL,dat,"Section Size");
	read_variables(dat,gpdwg);

	

	return 0;
}