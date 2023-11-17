// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/RoverCommand.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__ROVER_COMMAND__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__ROVER_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/rover_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_RoverCommand_turn
{
public:
  explicit Init_RoverCommand_turn(::interfaces::msg::RoverCommand & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::RoverCommand turn(::interfaces::msg::RoverCommand::_turn_type arg)
  {
    msg_.turn = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::RoverCommand msg_;
};

class Init_RoverCommand_steering
{
public:
  explicit Init_RoverCommand_steering(::interfaces::msg::RoverCommand & msg)
  : msg_(msg)
  {}
  Init_RoverCommand_turn steering(::interfaces::msg::RoverCommand::_steering_type arg)
  {
    msg_.steering = std::move(arg);
    return Init_RoverCommand_turn(msg_);
  }

private:
  ::interfaces::msg::RoverCommand msg_;
};

class Init_RoverCommand_throttle
{
public:
  explicit Init_RoverCommand_throttle(::interfaces::msg::RoverCommand & msg)
  : msg_(msg)
  {}
  Init_RoverCommand_steering throttle(::interfaces::msg::RoverCommand::_throttle_type arg)
  {
    msg_.throttle = std::move(arg);
    return Init_RoverCommand_steering(msg_);
  }

private:
  ::interfaces::msg::RoverCommand msg_;
};

class Init_RoverCommand_header
{
public:
  Init_RoverCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RoverCommand_throttle header(::interfaces::msg::RoverCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RoverCommand_throttle(msg_);
  }

private:
  ::interfaces::msg::RoverCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::RoverCommand>()
{
  return interfaces::msg::builder::Init_RoverCommand_header();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__ROVER_COMMAND__BUILDER_HPP_
