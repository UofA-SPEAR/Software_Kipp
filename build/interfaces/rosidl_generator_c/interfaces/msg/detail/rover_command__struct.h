// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/RoverCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ROVER_COMMAND__STRUCT_H_
#define INTERFACES__MSG__DETAIL__ROVER_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/RoverCommand in the package interfaces.
/**
  * std_msg/Header
  * https://docs.ros.org/en/melodic/api/std_msgs/html/msg/Header.html
  * Fill seq, note the limit of uint 32
  * Fill time stamp using epoch  
 */
typedef struct interfaces__msg__RoverCommand
{
  /// Includes a timestamp
  std_msgs__msg__Header header;
  /// Throttle command, range 0-1
  float throttle;
  /// Steering command, range -1 to 1
  float steering;
  /// Turn-in-place command, negative for left, positive for right
  float turn;
} interfaces__msg__RoverCommand;

// Struct for a sequence of interfaces__msg__RoverCommand.
typedef struct interfaces__msg__RoverCommand__Sequence
{
  interfaces__msg__RoverCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__RoverCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__DETAIL__ROVER_COMMAND__STRUCT_H_
