// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:srv/SerializePoseGraph.idl
// generated code does not contain a copyright notice

#ifndef SLAM_TOOLBOX__SRV__DETAIL__SERIALIZE_POSE_GRAPH__TRAITS_HPP_
#define SLAM_TOOLBOX__SRV__DETAIL__SERIALIZE_POSE_GRAPH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "slam_toolbox/srv/detail/serialize_pose_graph__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const SerializePoseGraph_Request & msg,
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
  const SerializePoseGraph_Request & msg,
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

inline std::string to_yaml(const SerializePoseGraph_Request & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::SerializePoseGraph_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::SerializePoseGraph_Request & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::SerializePoseGraph_Request>()
{
  return "slam_toolbox::srv::SerializePoseGraph_Request";
}

template<>
inline const char * name<slam_toolbox::srv::SerializePoseGraph_Request>()
{
  return "slam_toolbox/srv/SerializePoseGraph_Request";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SerializePoseGraph_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::srv::SerializePoseGraph_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<slam_toolbox::srv::SerializePoseGraph_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const SerializePoseGraph_Response & msg,
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
  const SerializePoseGraph_Response & msg,
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

inline std::string to_yaml(const SerializePoseGraph_Response & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::SerializePoseGraph_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::SerializePoseGraph_Response & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::SerializePoseGraph_Response>()
{
  return "slam_toolbox::srv::SerializePoseGraph_Response";
}

template<>
inline const char * name<slam_toolbox::srv::SerializePoseGraph_Response>()
{
  return "slam_toolbox/srv/SerializePoseGraph_Response";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SerializePoseGraph_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_toolbox::srv::SerializePoseGraph_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_toolbox::srv::SerializePoseGraph_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<slam_toolbox::srv::SerializePoseGraph>()
{
  return "slam_toolbox::srv::SerializePoseGraph";
}

template<>
inline const char * name<slam_toolbox::srv::SerializePoseGraph>()
{
  return "slam_toolbox/srv/SerializePoseGraph";
}

template<>
struct has_fixed_size<slam_toolbox::srv::SerializePoseGraph>
  : std::integral_constant<
    bool,
    has_fixed_size<slam_toolbox::srv::SerializePoseGraph_Request>::value &&
    has_fixed_size<slam_toolbox::srv::SerializePoseGraph_Response>::value
  >
{
};

template<>
struct has_bounded_size<slam_toolbox::srv::SerializePoseGraph>
  : std::integral_constant<
    bool,
    has_bounded_size<slam_toolbox::srv::SerializePoseGraph_Request>::value &&
    has_bounded_size<slam_toolbox::srv::SerializePoseGraph_Response>::value
  >
{
};

template<>
struct is_service<slam_toolbox::srv::SerializePoseGraph>
  : std::true_type
{
};

template<>
struct is_service_request<slam_toolbox::srv::SerializePoseGraph_Request>
  : std::true_type
{
};

template<>
struct is_service_response<slam_toolbox::srv::SerializePoseGraph_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__SRV__DETAIL__SERIALIZE_POSE_GRAPH__TRAITS_HPP_
