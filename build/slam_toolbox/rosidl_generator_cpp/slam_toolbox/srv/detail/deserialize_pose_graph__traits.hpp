// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_toolbox:srv/DeserializePoseGraph.idl
// generated code does not contain a copyright notice

#ifndef SLAM_TOOLBOX__SRV__DETAIL__DESERIALIZE_POSE_GRAPH__TRAITS_HPP_
#define SLAM_TOOLBOX__SRV__DETAIL__DESERIALIZE_POSE_GRAPH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "slam_toolbox/srv/detail/deserialize_pose_graph__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'initial_pose'
#include "geometry_msgs/msg/detail/pose2_d__traits.hpp"

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const DeserializePoseGraph_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: filename
  {
    out << "filename: ";
    rosidl_generator_traits::value_to_yaml(msg.filename, out);
    out << ", ";
  }

  // member: match_type
  {
    out << "match_type: ";
    rosidl_generator_traits::value_to_yaml(msg.match_type, out);
    out << ", ";
  }

  // member: initial_pose
  {
    out << "initial_pose: ";
    to_flow_style_yaml(msg.initial_pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DeserializePoseGraph_Request & msg,
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

  // member: match_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "match_type: ";
    rosidl_generator_traits::value_to_yaml(msg.match_type, out);
    out << "\n";
  }

  // member: initial_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "initial_pose:\n";
    to_block_style_yaml(msg.initial_pose, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DeserializePoseGraph_Request & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::DeserializePoseGraph_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::DeserializePoseGraph_Request & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::DeserializePoseGraph_Request>()
{
  return "slam_toolbox::srv::DeserializePoseGraph_Request";
}

template<>
inline const char * name<slam_toolbox::srv::DeserializePoseGraph_Request>()
{
  return "slam_toolbox/srv/DeserializePoseGraph_Request";
}

template<>
struct has_fixed_size<slam_toolbox::srv::DeserializePoseGraph_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<slam_toolbox::srv::DeserializePoseGraph_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<slam_toolbox::srv::DeserializePoseGraph_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace slam_toolbox
{

namespace srv
{

inline void to_flow_style_yaml(
  const DeserializePoseGraph_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DeserializePoseGraph_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DeserializePoseGraph_Response & msg, bool use_flow_style = false)
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
  const slam_toolbox::srv::DeserializePoseGraph_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_toolbox::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_toolbox::srv::to_yaml() instead")]]
inline std::string to_yaml(const slam_toolbox::srv::DeserializePoseGraph_Response & msg)
{
  return slam_toolbox::srv::to_yaml(msg);
}

template<>
inline const char * data_type<slam_toolbox::srv::DeserializePoseGraph_Response>()
{
  return "slam_toolbox::srv::DeserializePoseGraph_Response";
}

template<>
inline const char * name<slam_toolbox::srv::DeserializePoseGraph_Response>()
{
  return "slam_toolbox/srv/DeserializePoseGraph_Response";
}

template<>
struct has_fixed_size<slam_toolbox::srv::DeserializePoseGraph_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_toolbox::srv::DeserializePoseGraph_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_toolbox::srv::DeserializePoseGraph_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<slam_toolbox::srv::DeserializePoseGraph>()
{
  return "slam_toolbox::srv::DeserializePoseGraph";
}

template<>
inline const char * name<slam_toolbox::srv::DeserializePoseGraph>()
{
  return "slam_toolbox/srv/DeserializePoseGraph";
}

template<>
struct has_fixed_size<slam_toolbox::srv::DeserializePoseGraph>
  : std::integral_constant<
    bool,
    has_fixed_size<slam_toolbox::srv::DeserializePoseGraph_Request>::value &&
    has_fixed_size<slam_toolbox::srv::DeserializePoseGraph_Response>::value
  >
{
};

template<>
struct has_bounded_size<slam_toolbox::srv::DeserializePoseGraph>
  : std::integral_constant<
    bool,
    has_bounded_size<slam_toolbox::srv::DeserializePoseGraph_Request>::value &&
    has_bounded_size<slam_toolbox::srv::DeserializePoseGraph_Response>::value
  >
{
};

template<>
struct is_service<slam_toolbox::srv::DeserializePoseGraph>
  : std::true_type
{
};

template<>
struct is_service_request<slam_toolbox::srv::DeserializePoseGraph_Request>
  : std::true_type
{
};

template<>
struct is_service_response<slam_toolbox::srv::DeserializePoseGraph_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SLAM_TOOLBOX__SRV__DETAIL__DESERIALIZE_POSE_GRAPH__TRAITS_HPP_
