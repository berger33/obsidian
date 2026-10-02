---
id: software.testes.risk-based.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Risk-based testing, Teste baseado em risco, Priorização de testes por risco]
lote: software-testes-2000-0001
---

# Risk-based testing para priorizar o esforço

## Em uma frase
Teste baseado em risco usa riscos de produto e de projeto para decidir o que testar primeiro, com que profundidade e onde investir recursos limitados.

## Por que importa
Uma suíte extensa raramente pode ser executada integralmente em toda mudança. Priorizar por risco ajuda a concentrar tempo em falhas com maior probabilidade e consequência para usuários, negócio, segurança ou operação. Isso torna a seleção e a cobertura discutíveis e rastreáveis, em vez de depender apenas de ordem alfabética, preferência pessoal ou quantidade de casos.

## Como funciona
O ISTQB descreve risco de produto em termos de possibilidade de um evento adverso e suas consequências; a análise identifica e avalia riscos, enquanto o controle escolhe medidas para reduzi-los e acompanha o risco residual. Em teste, associa-se cada risco a condições, técnicas, dados e evidências pertinentes. O syllabus avançado trata risco como base para priorizar itens e selecionar técnicas e cobertura adequadas. A classificação deve refletir informação disponível, não falsa precisão matemática.

## Exemplo
Em uma mudança de checkout, uma falha de cálculo de imposto pode afetar muitos pedidos e gerar dano financeiro ou regulatório; uma diferença cosmética em texto de rodapé tende a ter outro impacto. A equipe pode executar primeiro os cenários de cálculo, arredondamento e combinações de região, depois cobrir riscos menores, registrando o que não coube no ciclo e o risco residual aceito.

## Limites e trade-offs
Estimativas de probabilidade e impacto são incertas e podem refletir vieses de quem participa. Um escore numérico não prova que todos os riscos importantes foram identificados; riscos novos surgem durante exploração, incidentes ou mudança de dependências. Priorizar não autoriza omitir silenciosamente requisitos de segurança, obrigações contratuais ou testes obrigatórios.

## Como verificar
Mantenha uma lista de riscos com justificativa, responsável, evidência, testes relacionados e data de reavaliação. Compare os riscos prioritários com a cobertura executada e documente aceitação de risco residual por quem tem autoridade. Atualize a ordem após mudanças, falhas encontradas, dados operacionais ou correções.

## Conexões
- [[regression-test-prioritization-risco-impacto]] — aplica priorização a uma suíte de regressão depois de mudanças.
- [[piramide-testes-estrategia-contexto]] — distribuição de níveis pode ser orientada por riscos.
- [[chaos-experiments-steady-state-blast-radius]] — experimentos de resiliência também precisam de hipóteses e limites de impacto.

## Fontes
- [ISTQB CTAL-TA Syllabus v4.0, capítulo 2](https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf) — análise e controle de risco no teste; acesso em 2026-10-01.
- [ISTQB/ASTQB CTFL Syllabus v4.0.1, seção 5.2](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — gestão de risco e risco de produto no processo de teste; acesso em 2026-10-01.
