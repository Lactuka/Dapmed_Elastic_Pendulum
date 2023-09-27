## Damped Elastic Pendulum
Let's calculate the Lagrangian for the elastic pendulum with no friction.

$\frac{d}{dt}(\frac{\partial L}{\partial\dot q_i}) - \frac{\partial L}{\partial q_i} = 0$ 

$T = \frac{1}{2}m \dot r^2 + \frac{1}{2}m(l+r)^2\dot \theta ^2$

$U = -mg(l+r)cos\theta + \frac{1}{2}kr^2$

$L = T-U = \frac{1}{2}m \dot r^2 + \frac{1}{2}m(l+r)^2\dot \theta ^2 + mg(l+r)cos\theta - \frac{1}{2}kr^2$

For $r$:

$\frac{\partial L}{\partial r} = mg cos\theta -kr +m(l+r)\dot \theta^2 $

$\frac{\partial L}{\partial \dot r} = m \dot r$

$m\ddot r - mg cos\theta + kr - m(l+r)\dot \theta^2$ = 0

$\ddot r = (l+r)\dot \theta^2 - \frac{k}{m}r + gcos\theta$ 

For $\theta$:

$\frac{\partial L}{\partial \theta} = -mg(l+r)sin\theta$ 

$\frac{\partial L}{\partial \dot \theta} = m(l+r)^2\dot \theta$

$\frac{d}{dt}(m(l+r)^2\dot \theta) = m \ddot \theta (l+r)^2 + 2m\dot\theta(l+r)\dot r$

$\ddot \theta (l+r) + 2\dot \theta \dot r + g sin\theta = 0$ 

$\ddot \theta = -(\frac{2\dot r \dot \theta + g sin\theta}{l+r})$

In the case of friction, our Euler-Lagrange equation becomes:

$\frac{d}{dt}(\frac{\partial L}{\partial\dot q_i}) - \frac{\partial L}{\partial q_i} = \frac{\partial F_f}{\partial \dot q_i}$

For a damping force that is proportional to velocity square, Our equations turn into these:

$\ddot r = (l+r)\dot \theta^2 - \frac{k}{m}r + gcos\theta - b \dot r$ 

$\ddot \theta = -(\frac{2\dot r \dot \theta + g sin\theta}{l+r}) - b \dot \theta$

Where $b$ is the damping coefficient with proper units.


## Animation

https://github.com/Lactuka/Elastic_Pendulum/assets/115004476/721975cf-a7c6-4f79-b444-8f661a11d7bc
