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
#include "libgpdwg.h"
#include "logger.h"
#include "version.h"
#include "variables.h"
#include <stdio.h>
#include <inttypes.h>
#include <stddef.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>

//int libgpdwg_loglevel = LOG_DEBUG;

void gpdwg_log_level(int level)
{
	libgpdwg_loglevel = level;
}





int gpdwg_load_file(char *filename, Bit_Data *dat)
{
	logger(LOG_DEBUG,0,0,"Stating file.");
	//Check file Stats.
	struct stat File_Stat;
	if(stat(filename, &File_Stat)==0)
	{

		printf("INFO  - Stating file.\n");
	}else{
		printf("ERROR - Could not get file stats. Check is file exists.\n");
		return -1;
	}
	if(!S_ISREG(File_Stat.st_mode))
	{
		printf("ERROR - Not a valid file.\n");
		return -1;
	}

	//Load file.
	FILE *dwg_file;
	dwg_file=fopen(filename,"rb");
	if(!dwg_file)
	{
		printf("ERROR - Can not read file.");
		return -1;
	}
	dat->byte = 0;
	dat->bit = 0;
	dat->size = File_Stat.st_size;
	dat->chain = (uint8_t *)malloc(dat->size);
	int read_size = 0;
	read_size = fread (dat->chain, sizeof (char), dat->size, dwg_file);
	if(read_size != dat->size)
	{
		printf("ERROR - Could not read complete file.\n");
		return -1;
	}
	if(read_size == 0)
	{
		printf("ERROR - Nothing to read in file.\n");
		return -1;
	}
	return 0;
}

int gpdwg_read(char *filename, Gpdwg_Data *gpdwg)
{
	// Load file in Bit Data.
	Bit_Data dat;
	int status = gpdwg_load_file(filename, &dat);

	// Check dwg version
	char version[7];
	strncpy (version, dat.chain, 8);
	version[6] = '\0';
	printf ("INFO  - File version is %s\n",version);
	
	if( strcmp(version,"AC1015") == 0)
	{
		status = decode_2000(&dat, gpdwg);
	}


	return 0;
}