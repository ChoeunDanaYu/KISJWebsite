import React, {Component} from 'react';
import {Button, View, Text} from 'react-native';

class AddEventScreen extends Component {
    render() {
        return(
            <View style={styles.container}>
                <Button title= "Event" onPress={() => this.props.navigation.navigate('Event Screen')}/>
            </View>
        )
    }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});