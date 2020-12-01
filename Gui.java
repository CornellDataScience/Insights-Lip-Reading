import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.Toolkit;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Gui extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Gui frame = new Gui();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Gui() {
		setResizable(false);
		setIconImage(Toolkit.getDefaultToolkit().getImage("C:\\Users\\gergo\\Desktop\\CDS.PNG"));
		setTitle("Insights Lip Reading");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JButton btnNewButton = new JButton();
		btnNewButton.setText("<html><center>" + "Capture" + "</center></html>");
		btnNewButton.setBounds(223, 231, 89, 33);
		contentPane.add(btnNewButton);

		JButton btnNewButton_1 = new JButton();
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		btnNewButton_1.setText("<html><center>" + "Read Lips" + "</center></html>");
		btnNewButton_1.setBounds(25, 231, 89, 33);
		contentPane.add(btnNewButton_1);

		JButton btnNewButton_2 = new JButton();
		btnNewButton_2.setText("<html><center>" + "Load File" + "</center></html>");
		btnNewButton_2.setBounds(322, 231, 89, 33);
		contentPane.add(btnNewButton_2);

		JButton btnNewButton_3 = new JButton();
		btnNewButton_3.setText("<html><center>" + "Crop Lips" + "</center></html>");
		btnNewButton_3.setBounds(124, 231, 89, 33);

		contentPane.add(btnNewButton_3);
	}
}
