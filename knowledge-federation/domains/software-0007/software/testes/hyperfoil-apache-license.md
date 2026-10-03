---
id: software.testes.tranche23.001731
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://hyperfoil.io/docs/overview/", "https://hyperfoil.io/", "https://hyperfoil.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Software livre para benchmarks auditáveis, Apache 2.0

## Em uma frase
A seção Free software do Overview oficial faz do licenciamento um argumento metodológico: "Free software allows you to take your benchmark and publish it for everyone to verify. With proprietary licenses that wouldn't be so easy" — e o Hyperfoil é distribuído sob a Apache License 2.0, com link para o texto.

## Por que importa
Benchmark sem verificação independente é marketing; a licença livre existe aqui para que o YAML do seu benchmark rode na máquina de outra pessoa byte a byte e a comparação pública seja possível sem acordos.

## Como funciona
A mesma seção posiciona o modelo de negócio dos concorrentes — ferramentas open-core cujo clustering é pago — como a razão de o Hyperfoil manter o modelo distribuído no núcleo licenciado, e a página inicial mantém o link GitHub como fonte primária.

## Exemplo
Adote a prática de versionar o .hf.yaml junto do relatório publicado; Apache-2.0 permite redistribuição do benchmark modificado sem relicenciamento, o que torna a auditoria por terceiros mecanicamente viável.

## Limites e trade-offs
A doc usa "free" no sentido de liberdade e licença; o texto não discute suporte comercial ou SLA, e verificar um benchmark continua exigindo o mesmo ambiente de alvo — a licença viabiliza, não padroniza a reproducibilidade.

## Como verificar
Abra a seção Free software do Overview oficial e confirme as duas frases citadas e o link da licença.

## Conexões
- [[hyperfoil-what-it-is]] — Veja também: Hyperfoil: framework distribuído de benchmark orientado a microsserviços.
- [[hyperfoil-open-system]] — Veja também: Modelo aberto contra coordinated omission: cada VU é uma máquina de estado.

## Fontes
- [Hyperfoil — Overview](https://hyperfoil.io/docs/overview/) — licença, distribuição, acurácia e versatilidade do DSL; consultado em 2026-10-03.
- [Hyperfoil — página inicial oficial](https://hyperfoil.io/) — definição e destaques distributed, accurate, versatile, low-allocation; consultado em 2026-10-03.
- [Hyperfoil — índice da documentação](https://hyperfoil.io/docs/) — nove seções: overview, quickstarts, user guide, API REST, extensions; consultado em 2026-10-03.
