---
id: software.testes.tranche23.001735
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
fontes: ["https://hyperfoil.io/docs/overview/concepts/", "https://hyperfoil.io/docs/overview/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Sessões pré-alocadas: o custo de não alocar no caminho quente

## Em uma frase
O modelo de estado do Hyperfoil é a session: "the state of each user's scenario is saved in the session; sometimes we speak about (re)starting sessions instead of starting new users" — e a página conecta a abstração diretamente com a política low-allocation: o benchmark pré-aloca toda a memória da execução do cenário adiante, o que implica que todos os recursos são limitados por pools (o sistema precisa saber os tamanhos).

## Por que importa
A conseqüência operacional é explícita na doc: é preciso declarar quantas sessions pré-alocar — a concorrência máxima do sistema — e quando o limite é ultrapassado o Hyperfoil até aloca sessions extras conforme necessário, mas a página crava que esse "is not the optimal mode of operation".

## Como funciona
A página diagnostica o que o estouro significa: ou você subestimou os recursos, ou colocou carga demais no alvo — requests que não completam e cenários que não terminam impedem a reciclagem dos objetos de sessão para o próximo usuário.

## Exemplo
Compare duas execuções do mesmo cenário, uma com pool abaixo e outra acima da concorrência efetiva: a primeira cresce requests e durações no stats (blocked/timeouts), enquanto a segunda mantém a reciclagem declarada na doc.

## Limites e trade-offs
O Concepts descreve o modelo de memória e seus sintomas, não os knobs numéricos do pool — a configuração de limites de session mora nas páginas de referência de steps e arquitetura da doc, citadas como seções separadas do site.

## Como verificar
Confirme na subseção Sessions do Concepts as frases da pré-alocação, do teto de concorrência e da reciclagem bloqueada.

## Conexões
- [[hyperfoil-phases]] — Veja também: Fases: workloads independentes, quatro estados, escala gradual.
- [[hyperfoil-scenario-steps]] — Veja também: Cenário = sequências = steps: a gramática do teste de carga.

## Fontes
- [Hyperfoil — Concepts](https://hyperfoil.io/docs/overview/concepts/) — controller e agents, fases, sessões e cenário/sequências/steps; consultado em 2026-10-03.
- [Hyperfoil — Overview](https://hyperfoil.io/docs/overview/) — licença, distribuição, acurácia e versatilidade do DSL; consultado em 2026-10-03.
