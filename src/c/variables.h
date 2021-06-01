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

#ifndef VARIABLES_H
#define VARIABLES_H

#include "libgpdwg.h"
#include "logger.h"
#include "bit.h"


int read_variables(Bit_Data *dat, Gpdwg_Data *gpdwg);
#endif