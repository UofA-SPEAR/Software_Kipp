// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:srv/AddSubmap.idl
// generated code does not contain a copyright notice

#ifndef SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_
#define SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "slam_toolbox/srv/detail/add_submap__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddSubmap_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: filename
  {
    out << "filename: ";
    rosidl_generator_traits::value_to_yaml(msg.filename, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddSubmap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: filename
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "filename: ";
    rosidl_generator_traits::value_to_yaml(msg.filename, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddSubmap_Request & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::AddSubmap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::AddSubmap_Request & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::AddSubmap_Request>()
{
  return "slam_toolbox::srv::AddSubmap_Request";
}

template<>
inline const char * name<slam_toolbox::srv::AddSubmap_Request>()
{
  return "slam_toolbox/srv/AddSubmap_Request";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<slam_toolbox::srv::AddSubmap_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddSubmap_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddSubmap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddSubmap_Response & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::AddSubmap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::AddSubmap_Response & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::AddSubmap_Response>()
{
  return "slam_toolbox::srv::AddSubmap_Response";
}

template<>
inline const char * name<slam_toolbox::srv::AddSubmap_Response>()
{
  return "slam_toolbox/srv/AddSubmap_Response";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_toolbox::srv::AddSubmap_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<slam_toolbox::srv::AddSubmap>()
{
  return "slam_toolbox::srv::AddSubmap";
}

template<>
inline const char * name<slam_toolbox::srv::AddSubmap>()
{
  return "slam_toolbox/srv/AddSubmap";
}

template<>
struct has_fixed_size<slam_toolbox::srv::AddSubmap>
  : std::integral_constant<
    bool,
    has_fixed_size<slam_toolbox::srv::AddSubmap_Request>::value &&
    has_fixed_size<slam_toolbox::srv::AddSubmap_Response>::value
  >
{
};

template<>
struct has_bounded_size<slam_toolbox::srv::AddSubmap>
  : std::integral_constant<
    bool,
    has_bounded_size<slam_toolbox::srv::AddSubmap_Request>::value &&
    has_bounded_size<slam_toolbox::srv::AddSubmap_Response>::value
  >
{
};

template<>
struct is_service<slam_toolbox::srv::AddSubmap>
  : std::true_type
{
};

template<>
struct is_service_request<slam_toolbox::srv::AddSubmap_Request>
  : std::true_type
{
};

template<>
struct is_service_response<slam_toolbox::srv::AddSubmap_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__SRV__DETAIL__ADD_SUBMAP__TRAITS_HPP_
