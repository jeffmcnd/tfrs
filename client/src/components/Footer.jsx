import React, { Component } from 'react';
import { Link } from 'react-router';

class Footer extends Component {
  render() {
    return (
      <div id="footer" role="contentinfo">
        <img className="back-to-top" src="./assets/images/back-to-top.png" alt="Back to top" title="Back to top" />
        <div id="footerWrapper">
          <div id="footerAdminSection">
            <div id="footerAdminLinksContainer" className="container">
              <div id="footerAdminLinks" className="row">
                <ul className="inline">
                  <li>
                    <a id="footer-home" href="#" target="_self">Home</a>
                  </li>
                  <li>
                    <a id="footer-about-site" href="#" target="_self">About this site</a>
                  </li>
                  <li>
                    <a id="footer-about-disclaimer" href="http://gov.bc.ca/disclaimer/" target="_self">Disclaimer</a>
                  </li>
                  <li>
                    <a id="footer-about-privacy" href="http://gov.bc.ca/privacy/" target="_self">Privacy</a>
                  </li>
                  <li>
                    <a id="footer-about-accessibility" href="http://gov.bc.ca/webaccessibility/" target="_self">Accessibility</a>
                  </li>
                  <li>
                    <a id="footer-about-copyright" href="http://gov.bc.ca/copyright" target="_self">Copyright</a>
                  </li>
                  <li>
                    <a id="footer-about-contact" href="#" target="_self">Contact Us</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Footer;