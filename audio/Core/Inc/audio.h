/*
 * audio.h
 *
 *  Created on: Dec 19, 2021
 *      Author: adria
 */
#include "main.h"
#ifndef INC_AUDIO_H_
#define INC_AUDIO_H_
#define AUDIO_RESET_PIN GPIO_PIN_4
#define AUDIO_I2C_ADDRESS 0x94

void init_AudioReset();
void configAudio();

#endif /* INC_AUDIO_H_ */
