---
id: software.devops.tranche16.001512
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/kapp/docs/v0.63.x/diff/", "https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md", "https://github.com/carvel-dev/kapp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel kapp: estágio de diff e estratégias de comparação contra `last-applied` versus recurso ativo

## Em uma frase
Durante o estágio de diff (`diff stage`), o `kapp` seleciona individualmente para cada recurso entre duas estratégias de comparação: comparar contra a última configuração aplicada pelo `kapp` (`kapp.k14s.io/original`) ou comparar diretamente contra o objeto vivo na API do Kubernetes.

## Por que importa
Controladores do cluster (como HorizontalPodAutoscaler, mutating webhooks de service mesh ou controladores de nuvem) modificam campos dos objetos após o deploy. Uma comparação ingênua contra o objeto vivo mostraria dezenas de linhas de ruído (campos adicionados por terceiros que não constam no arquivo local), dificultando a revisão humana ou auditoria em CI.

## Como funciona
Se o `kapp` detectar que nenhuma alteração externa ocorreu no recurso desde o último deploy, ele compara o novo manifesto contra a anotação `kapp.k14s.io/original`, produzindo um diff limpo e conciso. Caso detecte mudanças externas (drift), ele comuta automaticamente para a comparação contra o recurso vivo ou aplica regras de *rebase* (`rebaseRules`), podendo o operador forçar o comportamento global via `--diff-against-last-applied=bool`.

## Exemplo
```bash
kapp deploy -a payments-api -f rendered-manifests.yml --diff-changes --diff-run
kapp deploy -a payments-api -f rendered-manifests.yml --diff-against-last-applied=false --diff-run
```

## Limites e trade-offs
A flag `--diff-run` calcula e exibe o resumo completo de operações (`create`, `update`, `delete`, `noop`, `exists`) e o diff linha a linha sem aplicar nenhuma mudança no cluster, funcionando como um `plan` determinístico.

## Como verificar
Execute `kapp deploy -a payments-api -f rendered-manifests.yml --diff-changes --diff-run` em CI e verifique as colunas `Op`, `Op st.` e `Wait to` na tabela de resumo.

## Conexões
- [[carvel-kapp-agrupamento-recursos-labels-convergencia-client-side]] — Veja também: Carvel kapp: gerenciamento declarativo de aplicações Kubernetes por agrupamento de labels client-side.
- [[carvel-kapp-versioned-resources-configmap-secret-rollout]] — Veja também: Carvel kapp: recursos versionados (`kapp.k14s.io/versioned`) para rollout automático de ConfigMaps e Secrets.

## Fontes
- [Carvel kapp GitHub — README.md (Application Label Grouping, Diff & Apply Separation, Change Ordering & Non-Admin Operation)](https://carvel.dev/kapp/docs/v0.63.x/diff/) — README oficial do carvel-dev/kapp detalhando agrupamento por label, convergência de recursos, operação sem privilégios de admin e modo app-group GitOps; consultado em 2026-10-03.
- [Carvel kapp Official Documentation — Diff Stage v0.63.x (Diff Strategies, Last-Applied vs Live & Versioned Resources)](https://raw.githubusercontent.com/carvel-dev/kapp/develop/README.md) — Documentação oficial do estágio de diff do Carvel kapp cobrindo estratégias de comparação, recursos versionados (-ver-n) e templateRules; consultado em 2026-10-03.
- [Carvel kapp — Official GitHub Repository](https://github.com/carvel-dev/kapp) — Repositório oficial Apache-2.0 do Carvel kapp; consultado em 2026-10-03.
