# Copyright (C) 2007 by Cristobal Carnero Linan
# grendel.ccl@gmail.com
#
# This file is part of cvBlob.
#
# cvBlob is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cvBlob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with cvBlob.  If not, see <http://www.gnu.org/licenses/>.
#

# ----------------------------------------------------------------------------------
# NOTE - zorzalzilba  
# This file is a python version of the original C++ test/test.cpp
# Where possible, python code is listed along side the original line(s) of C++ code.
# ----------------------------------------------------------------------------------

# Import opencv and cvblob python extensions
# Note: these must be findable on PYTHONPATH
import cv
import cvblob


# IplImage *img = cvLoadImage("test.png", 1);
img = cv.LoadImage("../../../../test/test.png",1)

#cvSetImageROI(img, cvRect(100, 100, 800, 500));
cv.SetImageROI(img, (100, 100, 800, 500))

#IplImage *grey = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);
grey = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_8U,1)

#cvCvtColor(img, grey, CV_BGR2GRAY);
cv.CvtColor(img, grey, cv.CV_BGR2GRAY)

#cvThreshold(grey, grey, 100, 255, CV_THRESH_BINARY);
cv.Threshold(grey, grey, 100, 255, cv.CV_THRESH_BINARY)

#IplImage *labelImg = cvCreateImage(cvGetSize(grey),IPL_DEPTH_LABEL,1);
IPL_DEPTH_LABEL = 32
labelImg = cv.CreateImage(cv.GetSize(grey), IPL_DEPTH_LABEL, 1)

#CvBlobs blobs;
blobs = cvblob.CvBlobs()

#unsigned int result = cvLabel(grey, labelImg, blobs);
result = cvblob.cvLabel(grey,labelImg,blobs)

#IplImage *imgOut = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 3);
imgOut = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_8U,3)
cv.Zero(imgOut);

#cvRenderBlobs(labelImg, blobs, img, imgOut);
cvblob.cvRenderBlobs(labelImg, blobs, img, imgOut);


#
#//unsigned int i = 0;
#
#// Render contours:
# for (CvBlobs::const_iterator it=blobs.begin(); it!=blobs.end(); ++it) {

for label, blob in blobs.iteritems(): 


#    //cvRenderBlob(labelImg, (*it).second, img, imgOut);
# 
#   CvScalar meanColor = cvBlobMeanColor((*it).second, labelImg, img);
    meanColor = cvblob.cvBlobMeanColor(blob, labelImg, img)

#   cout << "Mean color: r=" << (unsigned int)meanColor.val[0] << ", g=" << (unsigned int)meanColor.val[1] << ", b=" << (unsigned int)meanColor.val[2] << endl;
    print "Mean color: r=" + str(meanColor[0]) + ", g=" + str(meanColor[1]) + ", b=" + str(meanColor[2])

#   CvContourPolygon *polygon = cvConvertChainCodesToPolygon(&(*it).second->contour);
# 
#   CvContourPolygon *sPolygon = cvSimplifyPolygon(polygon, 10.);
#   CvContourPolygon *cPolygon = cvPolygonContourConvexHull(sPolygon);
# 
#   cvRenderContourChainCode(&(*it).second->contour, imgOut);
#   cvRenderContourPolygon(sPolygon, imgOut, CV_RGB(0, 0, 255));
#   cvRenderContourPolygon(cPolygon, imgOut, CV_RGB(0, 255, 0));
# 
#   delete cPolygon;
#   delete sPolygon;
#   delete polygon;
# 
#   // Render internal contours:
#   for (CvContoursChainCode::const_iterator jt=(*it).second->internalContours.begin(); jt!=(*it).second->internalContours.end(); ++jt)
#       cvRenderContourChainCode((*jt), imgOut);
# 
#   //stringstream filename;
#   //filename << "blob_" << setw(2) << setfill('0') << i++ << ".png";
#   //cvSaveImageBlob(filename.str().c_str(), imgOut, (*it).second);
# }
# 
# cvNamedWindow("test", 1);
# cvShowImage("test", imgOut);
# //cvShowImage("grey", grey);
# cvWaitKey(0);
# cvDestroyWindow("test");
# 
# cvReleaseImage(&imgOut);
# cvReleaseImage(&grey);
# cvReleaseImage(&labelImg);
# cvReleaseImage(&img);
# 
# cvReleaseBlobs(blobs);
# 