---
id: software.testes.exploratory.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://astqb.org/4-4-experience-based-test-techniques/", "https://satisfice.us/articles/et-article.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Exploratory testing, Teste exploratório, Teste baseado em exploração]
lote: software-testes-2000-0001
---

# Exploratory testing: aprender enquanto se testa

## Em uma frase
Teste exploratório integra aprendizado sobre o produto, desenho de testes, execução e avaliação, usando evidências de cada ação para orientar a próxima.

## Por que importa
Casos totalmente especificados antes da execução são úteis para repetição e rastreabilidade, mas podem não explorar bem requisitos ambíguos, comportamentos inesperados ou informações recém-descobertas. Na exploração, o tester ajusta hipóteses e entradas com base nas respostas observadas, o que pode revelar riscos ainda não descritos em scripts.

## Como funciona
O syllabus ISTQB define que os testes são desenhados, executados e avaliados simultaneamente enquanto a pessoa aprende sobre o item. James Bach descreve a prática como um contínuo entre procedimentos altamente prescritos e exploração mais livre, não como ausência obrigatória de planejamento. Uma missão ou charter delimita área, risco ou pergunta; notas registram ações relevantes, observações, dúvidas e defeitos para comunicar resultados e derivar testes repetíveis quando apropriado.

## Exemplo
Ao explorar uma tela de recuperação de senha, a missão pode investigar respostas a tentativas repetidas, endereços malformados e links expirados. Se a observação revelar que um token continua válido após uso, a pessoa registra a sequência e o contexto, confirma a repetibilidade e encaminha um defeito; depois, um caso automatizado pode proteger a regressão.

## Limites e trade-offs
Exploração sem objetivo, conhecimento compartilhado ou registro adequado pode deixar cobertura difícil de avaliar e descobertas difíceis de reproduzir. Uma sessão curta não demonstra ausência de defeitos. Testes exploratórios não substituem verificações repetidas necessárias, requisitos regulatórios ou automatização adequada; scripts também não substituem investigação humana em todos os contextos.

## Como verificar
Defina missão e limites de segurança antes da sessão. Registre ambiente, dados, ações relevantes, observações, bugs e áreas não cobertas; ao terminar, avalie quais riscos foram investigados e quais seguem abertos. Transforme descobertas de alto valor em testes repetíveis quando houver benefício de manutenção.

## Conexões
- [[session-based-testing-charters-debriefs]] — acrescenta estrutura de sessões e debrief ao trabalho exploratório.
- [[risk-based-testing-priorizacao-risco]] — ajuda a escolher as missões de maior risco.
- [[test-oracles-resultados-esperados]] — exploração também depende de critérios ou conhecimento para avaliar resultados.

## Fontes
- [ASTQB/ISTQB CTFL — Experience-based Test Techniques, seção 4.4.2](https://astqb.org/4-4-experience-based-test-techniques/) — definição e objetivo do teste exploratório; acesso em 2026-10-01.
- [James Bach — Exploratory Testing Explained](https://satisfice.us/articles/et-article.pdf) — estrutura situacional, espectro entre scripts e exploração, e uso de charters; acesso em 2026-10-01.
