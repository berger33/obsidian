---
id: software.testes.testing-debugging.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/1-1-what-is-testing/", "https://astqb.org/1-2-why-is-testing-necessary/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Testing versus debugging, Testing and debugging, Teste e depuração]
lote: software-testes-2000-0001
---

# Teste e debugging são atividades distintas

## Em uma frase
Teste procura evidência sobre a qualidade e pode revelar defeitos; debugging investiga e remove a causa de uma falha observada ou de um defeito encontrado.

## Por que importa
Quando uma falha é observada, executar novamente o mesmo caso pode confirmar que ela se repete, mas não explica sua origem. Confundir teste com correção dificulta definir papéis e registrar evidência. Separar as atividades também deixa claro que “teste falhou” descreve um resultado, enquanto debugging procura o defeito que o causou.

## Como funciona
O CTFL distingue testes estáticos, que podem localizar defeitos diretamente em work products, e testes dinâmicos, que executam o software e podem desencadear falhas causadas por defeitos. Após uma falha dinâmica, debugging normalmente reproduz o problema, diagnostica a causa e corrige o defeito. Um teste de confirmação então verifica se a correção resolveu o problema; regressão verifica se mudanças afetaram outras partes.

## Exemplo
Um teste automatizado recebe uma exceção inesperada ao enviar uma solicitação. O log, a entrada e a versão são evidência do teste. A pessoa que depura reproduz, localiza um erro no tratamento de timeout e altera o código. Em seguida, o teste de confirmação verifica o caminho corrigido e uma seleção de regressão cobre comportamentos relacionados.

## Limites e trade-offs
A pessoa que executou o teste pode também depurar; a distinção é entre atividades, não necessariamente entre pessoas. Um teste que passa após a correção não demonstra que a causa foi corretamente removida de todos os caminhos. Para defeitos encontrados estaticamente pode não haver falha a reproduzir; o work product é inspecionado diretamente.

## Como verificar
Registre falha observada, precondições, dados e versões antes da correção. Mantenha separadas hipótese de causa, alteração feita e evidência dos testes de confirmação/regressão. Se o caso não reproduzir, investigue diferenças ambientais em vez de apagar o relato.

## Conexões
- [[test-oracles-resultados-esperados]] — distingue resultado esperado do que foi observado.
- [[defect-report-reproducibility-severity-priority]] — registra contexto para reproduzir e triar anomalias.
- [[regression-test-prioritization-risco-impacto]] — ajuda a selecionar verificações após uma correção.

## Fontes
- [ASTQB — ISTQB CTFL §1.1: What is Testing?](https://astqb.org/1-1-what-is-testing/) — separação entre teste e debugging e passos típicos; acesso em 2026-10-01.
- [ASTQB — ISTQB CTFL §1.2: Why is Testing Necessary?](https://astqb.org/1-2-why-is-testing-necessary/) — contribuição do teste e distinção da atividade de correção; acesso em 2026-10-01.
