import React, { PropTypes } from 'react';
import styles from './NameLabel.css';
import withViewport from '../../decorators/withViewport';
import withStyles from '../../decorators/withStyles';
import Link from '../Link';

@withViewport
@withStyles(styles)
class NameLabel {

  static propTypes = {
    viewport: PropTypes.shape({
      width: PropTypes.number.isRequired,
      height: PropTypes.number.isRequired
    }).isRequired
  };

  render() {
    return (
      <div className="NameLabel">
        <div className="NameLabel-container">
          <div className="NameLabel-text">Andrew Demoleas</div>
        </div>
      </div>
    );
  }

}

export default NameLabel;
