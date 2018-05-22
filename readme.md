# Face Recognition via Sparse Representation-based Classification (SRC) #

## 申明 ##

Code仅用于学术研究目的，商业使用上的版权问题本人概不负责。有任何的学术方面的讨论，欢迎邮件409544320@qq.com。

Code中使用了[OpenCV](http://opencv.org/ "OpenCV")进行底层图像处理，使用了[Fast l-1 Minimization Algorithms: Homotopy and Augmented Lagrangian Method -- Implementation from Fixed-Point MPUs to Many-Core CPUs/GPUs, by Allen Y. Yang, Arvind Ganesh, Zihan Zhou, Andrew Wagner, Victor Shia, Shankar Sastry, and Yi Ma](http://www.eecs.berkeley.edu/~yang/software/l1benchmark/ "l1min")进行l-1 Minimization优化。后者申明：

    /*% README
    % Copyright ©2010. The Regents of the University of California (Regents).
    % All Rights Reserved. Contact The Office of Technology Licensing,
    % UC Berkeley, 2150 Shattuck Avenue, Suite 510, Berkeley, CA 94720-1620,
    % (510) 643-7201, for commercial licensing opportunities.

    % Created by Victor Shia, Allen Y. Yang, Department of EECS, University of California,
    % Berkeley.

    % IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
    % SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS,
    % ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF
    % REGENTS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    % REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED
    % TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
    % PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY,
    % PROVIDED HEREUNDER IS PROVIDED "AS IS". REGENTS HAS NO OBLIGATION TO
    % PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
    */

    README file for DALM/PALM and Homotopy l1-minimization code
    by Victor Shia, Allen Yang

## 文件说明 ##

**./paper目录** 两篇有关Sparse Representation-based Classification(SRC)算法的原理

* PAMI-Face.pdf -> SRC原理
* YangA\_ICIP2010.pdf -> SRC中涉及的L1-Min问题解法，包括DALM算法等

**./codes目录** SRC algorithm is implemented concretely
					
* slib// The Static library project includes the main implementation of SRC algorithm, in which the fast Dalm algorithm for l1-min problem is used.
* train exe// The project realizes the training program of SRC, using see program usage
* test exe// The project realizes the test procedure of SRC, using see program usage
* test.py// File (./codes/face_recog. src/_exe/test.py) implements 	the batch processing test function of SRC algorithm
* ./codes/face\_recog.SRC/\_exe/extYaleB Table of Contents is [Extended Yale face Database B Facial database](http://vision.ucsd.edu/~leekc/ExtYaleDatabase/ExtYaleB.html "yalefacedb")


409544320@qq.com, 6/11/2011
