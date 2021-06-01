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
#include "logger.h"
#include <stdio.h>



void logger(const int level, const int pos_byte,const int pos_bit, const char *strMessage)
{
	if (level <= libgpdwg_loglevel)
	{
		switch(level)
		{
			case 1:
				fprintf(stderr,"ERROR %i - %i %s\n", pos_byte, pos_bit,strMessage);
				break;
			case 2:
				fprintf(stderr,"INFO %i - %i %s\n", pos_byte, pos_bit,strMessage);
				break;
			case 3:
				fprintf(stderr,"DEBUG: %i - %i %s\n", pos_byte, pos_bit,strMessage);
				break;
		}
	}
}