package com.github.thiagotgm.forester;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {

    /**
     * Rigorous Test :-)
     */
    @Tag( "unit" )
    @Test
    public void testUT() {

        System.out.println( "Unit test" );
        assertTrue( true );

    }
    
    @Tag( "integration" )
    @Test
    public void testIT() {
        
        System.out.println( "Integration test" );
        assertTrue( true );
        
    }

}
