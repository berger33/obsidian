---
id: software.testes.combinatorial.000001
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
fontes: ["https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf", "https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software/downloadable-tools"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Combinatorial testing, Pairwise testing, T-way testing, Teste combinatório]
lote: software-testes-2000-0001
---

# Combinatorial testing: pairwise e cobertura t-way

## Em uma frase
Teste combinatório constrói um conjunto reduzido de casos que cobre combinações de valores de parâmetros até uma força de interação t escolhida.

## Por que importa
Falhas podem depender de uma combinação de configurações que, isoladamente, parece válida — por exemplo, navegador, sistema operacional e protocolo. Testar o produto cartesiano completo pode ser caro; um covering array pode cobrir todos os pares ou todas as combinações de t fatores com menos casos. A redução é uma estratégia de seleção, não uma garantia de detectar todos os defeitos.

## Como funciona
Definem-se fatores e valores discretos para cada fator. Em pairwise, cada par de valores de dois fatores precisa ocorrer pelo menos uma vez em algum caso; em t-way, a propriedade estende-se a t fatores. Ferramentas do NIST, como ACTS, geram conjuntos para cobertura t-way e podem considerar restrições entre valores. Combinações impossíveis devem ser declaradas para que a cobertura se refira às configurações válidas.

## Exemplo
Considere três fatores de configuração: navegador, sistema operacional e protocolo. Um par de fatores por vez pode ser coberto por poucos casos em comparação com executar toda combinação possível. Se um navegador não existe em determinado sistema operacional, declare essa restrição; depois, confirme que todos os pares válidos ainda aparecem na suíte gerada.

## Limites e trade-offs
Pairwise não cobre necessariamente defeitos acionados por interações de ordem maior; a escolha de t deve refletir risco, conhecimento de domínio e custo. Restrições incorretas removem combinações que poderiam ser relevantes. A cobertura calculada pela ferramenta depende do modelo fornecido e não valida por si só os resultados esperados de cada caso.

## Como verificar
Revise fatores, valores e constraints com as pessoas responsáveis pela configuração. Gere a suíte e use uma medição de cobertura combinatória para conferir a força e a cobertura de todas as combinações válidas. Inspecione manualmente casos removidos ou inviáveis, associe cada teste a um resultado esperado e preserve regressões descobertas.

## Conexões
- [[decision-table-testing-regras-condicionais]] — tabelas explícitas de regras são apropriadas quando as combinações determinam ações específicas.
- [[particionamento-equivalencia-valores-fronteira]] — reduz valores por classe antes de construir combinações.
- [[testes-stateful-model-based-hypothesis]] — stateful testing gera sequências de ações; t-way normalmente cobre combinações de fatores.

## Fontes
- [ISTQB CTAL-TA Syllabus v4.0, seção 3.1.2](https://www.gasq.org/files/content/ISTQB2/ISTQB-CTAL-TA-Syllabus-v4.0-EN.pdf) — cobertura de interações multidimensionais por combinatorial testing; acesso em 2026-10-01.
- [NIST — ACTS Downloadable Tools](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software/downloadable-tools) — geração de cobertura t-way, constraints e variable-strength tests; acesso em 2026-10-01.
