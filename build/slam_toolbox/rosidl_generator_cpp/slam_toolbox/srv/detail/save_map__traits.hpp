// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:srv/SaveMap.idl
// generated code does not contain a copyright notice

#ifndef SLAM_TOOLBOX__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_
#define SLAM_TOOLBOX__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "slam_toolbox/srv/detail/save_map__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'name'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const SaveMap_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    to_flow_style_yaml(msg.name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SaveMap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name:\n";
    to_block_style_yaml(msg.name, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SaveMap_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

[[deprecated("use slam_toolbox::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const slam_toolbox::srv::SaveMap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::SaveMap_Request & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::SaveMap_Request>()
{
  return "slam_toolbox::srv::SaveMap_Request";
}

template<>
inline const char * name<slam_toolbox::srv::SaveMap_Request>()
{
  return "slam_toolbox/srv/SaveMap_Request";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SaveMap_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<slam_toolbox::srv::SaveMap_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<slam_toolbox::srv::SaveMap_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const SaveMap_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SaveMap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SaveMap_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace slam_toolbox

namespace rosidl_generator_traits
{

[[deprecated("use slam_toolbox::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const slam_toolbox::srv::SaveMap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::SaveMap_Response & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::SaveMap_Response>()
{
  return "slam_toolbox::srv::SaveMap_Response";
}

template<>
inline const char * name<slam_toolbox::srv::SaveMap_Response>()
{
  return "slam_toolbox/srv/SaveMap_Response";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SaveMap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_toolbox::srv::SaveMap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_toolbox::srv::SaveMap_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<slam_toolbox::srv::SaveMap>()
{
  return "slam_toolbox::srv::SaveMap";
}

template<>
inline const char * name<slam_toolbox::srv::SaveMap>()
{
  return "slam_toolbox/srv/SaveMap";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SaveMap>
  : std::integral_constant<
    bool,
    has_fixed_size<slam_toolbox::srv::SaveMap_Request>::value &&
    has_fixed_size<slam_toolbox::srv::SaveMap_Response>::value
  >
{
};

template<>
struct has_bounded_size<slam_toolbox::srv::SaveMap>
  : std::integral_constant<
    bool,
    has_bounded_size<slam_toolbox::srv::SaveMap_Request>::value &&
    has_bounded_size<slam_toolbox::srv::SaveMap_Response>::value
  >
{
};

template<>
struct is_service<slam_toolbox::srv::SaveMap>
  : std::true_type
{
};

template<>
struct is_service_request<slam_toolbox::srv::SaveMap_Request>
  : std::true_type
{
};

template<>
struct is_service_response<slam_toolbox::srv::SaveMap_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_
