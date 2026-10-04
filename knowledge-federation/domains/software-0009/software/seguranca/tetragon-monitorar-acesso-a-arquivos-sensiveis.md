---
id: software.seguranca.tranche18.001758
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://tetragon.io/docs/concepts/tracing-policy/", "https://tetragon.io/docs/concepts/tracing-policy/mode/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cilium Tetragon: Monitorar acesso a arquivos sensíveis

## Em uma frase
**Cilium Tetragon — Monitorar acesso a arquivos sensíveis:** Uma policy pode observar tentativas de leitura ou escrita em caminhos e chamar atenção para acesso inesperado.

## Por que importa
O recorte de **monitorar acesso a arquivos sensíveis** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **monitorar acesso a arquivos sensíveis**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Monitore acesso a arquivo de laboratório e associe evento ao processo e identidade do pod. Teste em staging autorizado.

## Limites e trade-offs
Caminho de arquivo pode variar por container, symlink ou namespace de montagem. Exceções exigem responsável e prazo.

## Como verificar
Gere eventos permitidos e negados em container descartável e compare o campo path. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-avaliar-conexao-de-rede-por-processo]] — Complementa o tópico com cilium tetragon: avaliar conexão de rede por processo.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
