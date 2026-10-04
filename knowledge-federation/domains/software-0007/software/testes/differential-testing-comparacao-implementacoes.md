---
id: software.testes.differential.000001
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
fontes: ["https://releases.llvm.org/3.4/docs/TestingGuide.html", "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Differential testing, Differential test, Teste diferencial]
lote: software-testes-2000-0001
---

# Differential testing: comparar implementações equivalentes

## Em uma frase
Teste diferencial executa implementações que deveriam obedecer ao mesmo contrato com a mesma entrada e investiga divergências entre seus resultados.

## Por que importa
Quando calcular manualmente o resultado esperado é difícil, uma implementação independente pode servir de ponto de comparação. Essa estratégia é usada, por exemplo, em compiladores, parsers, serializadores e validação de certificados. Divergência revela que pelo menos uma execução merece investigação, sem identificar automaticamente qual implementação está correta.

## Como funciona
Escolhem-se implementações independentes ou configurações de compilação que afirmam a mesma semântica. Cada uma recebe entradas equivalentes; as saídas são normalizadas apenas para diferenças legítimas, como ordem não especificada, e comparadas. O guia histórico do LLVM descreve comparar a saída de programas compilados com uma saída de referência; isso é um exemplo de comparação diferencial contra golden output, não evidência por si só de comparação entre implementações independentes. O artigo do NIST sobre testes metamórficos descreve validadores de certificados independentes como exemplo de comparação entre implementações e recomenda investigar divergências.

## Exemplo
Um gerador de casos cria certificados X.509. O teste executa validadores independentes com a mesma cadeia e política, recolhe a decisão e detalhes normalizados e destaca divergências. Uma divergência não basta para declarar um defeito: confira requisitos, versões, configuração e se as implementações realmente compartilham a mesma expectativa.

## Limites e trade-offs
Implementações podem compartilhar código ou suposições erradas, produzindo concordância sem correção. Diferenças legítimas de formato, opções, precisão ou ambiente geram falsos positivos se não forem normalizadas com cuidado. Não use votação por maioria como substituto de uma especificação: várias implementações podem compartilhar o mesmo bug.

## Como verificar
Confirme independência suficiente e equivalência de configurações; preserve a entrada que divergiu. Classifique resultados esperados, erros e diferenças toleradas. Reproduza com versão/configuração fixas e compare contra especificação ou oracle confiável antes de corrigir. Acrescente o caso à suíte após estabelecer o resultado correto.

## Conexões
- [[metamorphic-testing-oracle-relations]] — compara saídas de execuções relacionadas de uma implementação, em vez de depender apenas de pares de implementações.
- [[testes-hermeticos-dependencias]] — versões e ambiente das implementações comparadas precisam ser controlados.
- [[fuzzing-coverage-guided-libfuzzer]] — entradas fuzzed podem alimentar comparações diferenciais.

## Fontes
- [LLVM 3.4 — Testing Infrastructure Guide](https://releases.llvm.org/3.4/docs/TestingGuide.html) — comparação de programas compilados e saídas de referência; acesso em 2026-10-01.
- [NIST — Metamorphic Testing for Cybersecurity](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920197) — exemplo de discrepâncias entre validadores independentes de certificados; acesso em 2026-10-01.
