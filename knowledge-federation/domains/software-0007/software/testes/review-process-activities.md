---
id: software.testes.review-process.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/3-2-feedback-and-review-process/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Review process activities, Software review process, Processo de revisão]
lote: software-testes-2000-0001
---

# Atividades de um processo de revisão

## Em uma frase
Uma revisão pode estruturar planejamento, início, leitura individual, comunicação/análise e correção/relato, ajustando formalidade à situação.

## Por que importa
Reuniões sem objetivo, preparação ou follow-up podem consumir tempo e deixar defeitos sem responsável. Um processo claro define o work product, foco, participantes, como registrar findings e como tratar correções, sem impor a mesma formalidade a toda revisão.

## Como funciona
O CTFL se apoia no processo genérico da ISO/IEC 20246: planejar escopo e objetivos; iniciar/distribuir o material; permitir revisão individual; comunicar e analisar findings; corrigir e reportar. Para trabalhos grandes, o processo pode ser repetido por partes. Uma revisão mais formal executa mais tarefas e documenta mais elementos; a revisão específica deve ser adaptada aos riscos, tipo de artefato e necessidades do projeto.

## Exemplo
Para uma especificação de API, o líder delimita endpoints e critérios de consistência, envia o material e checklist, recolhe comentários individuais, discute ambiguidades, registra decisões e encaminha correções. Se o contrato for grande, divide-o por grupos de operações em ciclos manejáveis.

## Limites e trade-offs
Formalidade excessiva aumenta custo em mudanças pequenas; informalidade pode ser inadequada quando há auditoria, criticidade ou necessidade de evidência. Revisão não é prova de que o documento não contém defeitos. Findings devem ser triados contra objetivo, não todos tratados como igual prioridade.

## Como verificar
Confirme que objetivo, escopo, participantes, preparação e critérios de saída estavam claros. Verifique se findings têm decisão e dono, correções foram confirmadas e resultado foi comunicado. Revise o próprio processo se revisões recorrentes deixam problemas semelhantes.

## Conexões
- [[static-testing-work-products]] — revisões são uma forma de teste estático.
- [[review-types-formality-purpose]] — escolhe tipo de revisão para objetivos e contexto.
- [[defect-report-reproducibility-severity-priority]] — findings que exigem mudança podem virar relatórios de defeito.

## Fontes
- [ASTQB — ISTQB CTFL §3.2: Feedback and Review Process](https://astqb.org/3-2-feedback-and-review-process/) — cinco atividades do processo genérico e tailoring; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 3.2.2, atividades do processo genérico de revisão; acesso em 2026-10-01.
