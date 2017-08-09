import numpy as np

#
# Quaternion conversions transcribed from Wikipedia
#

def get_phi( q0 , q1 , q2 , q3 ):
    return np.arctan2( 2.0*((q0*q1) + (q2*q3)) , 1.0 - 2.0*((q1*q1) + (q2*q2)) )

def get_theta( q0 , q1 , q2 , q3 ):
    return np.arcsin( 2.0*((q0*q2) - (q3*q1)) )
                     
def get_psi( q0 , q1 , q2 , q3 ):
    return np.arctan2( 2.0*((q0*q3) + (q1*q2)) , 1.0 - 2.0*((q2*q2) + (q3*q3)) )

# Normalize all quaternions in DataFrame
def normalize_df( df , q0='Q0' , q1='Q1' , q2='Q2' , q3='Q3' ):
    mag = np.sqrt( (df[q0]*df[q0]) + (df[q1]*df[q1]) + (df[q2]*df[q2]) + (df[q3]*df[q3]) )
    df[q0] = df[q0] / mag
    df[q1] = df[q1] / mag
    df[q2] = df[q2] / mag
    df[q3] = df[q3] / mag

# compute "pendulum" angle w.r.t. x-y plane
# Derive by creating a z-axis unit vector, rotate it by the quaternion, and compute
# the angle between the initial unit vector and the rotated vector:
#   init_unit_vector *dot* rotated_unit_vector = cos(angle)
def get_xyangle( q0 , q1 , q2 , q3 ):
    return np.arccos( (q0*q0) + (q3*q3) - (q1*q1) - (q2*q2) )
    
# Normalize quatnerion vector (in case it's not already normalized)
def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = math.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

# function to return conjugate quaternion
def q_conjugate( q ):
    return (q[0], -q[1], -q[2], -q[3])

# return the product of two quaternions
def q_mult( q1 , q2 ):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return (w, x, y, z)

# Quaternion vector multiplication
def qv_mult( q1 , v1 ):
    # convert vector into quaternion by prepending a 0
    q2 = (0.0,) + v1
    return q_mult( q_mult(q1,q2) , q_conjugate(q1) )[1:]

# convert a vector and angle to a quaternion
def axisangle_to_q( v , theta ):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = math.cos(theta)
    x = x * math.sin(theta)
    y = y * math.sin(theta)
    z = z * math.sin(theta)
    return (w, x, y, z)

# convert a quaternion to a unit vector and an angle
def q_to_axisangle( q ):
    w, v = q[0], q[1:]
    theta = math.acos(w) * 2.0
    return normalize(v), theta

# Get angle of quaternion w.r.t. the x-y plane
# We create a z-axis unit vector, rotate it by the quaternion, and compute
# the angle between the initial unit vector and the rotated vector:
#   init_unit_vector *dot* rotated_unit_vector = cos(angle)
def q_angle_xyplane( q ):
    return math.acos( qv_mult( q , (0,0,1) )[2] )
