      * Copyright (c) 2024 Broadcom.
      * The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
      *
      * This program and the accompanying materials are made
      * available under the terms of the Eclipse Public License 2.0
      * which is available at https://www.eclipse.org/legal/epl-2.0/
      *
      * SPDX-License-Identifier: EPL-2.0
      *
      * Contributors:
      *    Broadcom, Inc. - initial API and implementation
      *
       IDENTIFICATION DIVISION.
       PROGRAM-ID. EVAL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NUM1 PIC 9(9).
       PROCEDURE DIVISION.
           PERFORM UNTIL WS-NUM1 IS EQUAL "A"
               EXIT PERFORM
               EXIT PERFORM CYCLE
               GO TO PAR1
           END-PERFORM.
           EXIT PERFORM.
       PAR1.
           CONTINUE.