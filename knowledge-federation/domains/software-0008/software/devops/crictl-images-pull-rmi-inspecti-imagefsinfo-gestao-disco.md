---
id: software.devops.tranche14.001395
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md", "https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md", "https://github.com/kubernetes-sigs/cri-tools"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# crictl: Gestão de Imagens e Diagnóstico de Disco no Nó (images, inspecti, imagefsinfo, pull e rmi)

## Em uma frase
A família de comandos de imagem do `crictl` (`images`, `inspecti`, `imagefsinfo`, `pull` e `rmi`) permite auditar todas as imagens em cache no nó, testar o pull autenticado (`--creds` / `--auth`) diretamente pelo CRI e inspecionar o uso do sistema de arquivos de imagens (`imagefsinfo`).

## Por que importa
Quando o `kubelet` reporta a condição `DiskPressure` na partição `imagefs` do nó, o operador precisa identificar rapidamente quais imagens ocupam mais espaço e remover imagens não utilizadas (`crictl rmi --prune`).

## Como funciona
O comando `crictl imagefsinfo` retorna a capacidade e os bytes utilizados pelo filesystem de imagens do runtime; `crictl images -v` lista os digests, tags e tamanhos; `crictl inspecti <image-id>` exibe camadas e configurações da imagem; e `crictl rmi --prune` limpa imagens que não estão referenciadas por nenhum container existente.

## Exemplo
```bash
crictl imagefsinfo
crictl images -v
crictl rmi --prune
```

## Limites e trade-offs
Executar `crictl rmi <image>` em uma imagem base que está sendo referenciada por um container parado (`Exited`) falha até que o container parado seja removido ou que o `--prune` ignore imagens em uso.

## Como verificar
Use `crictl rmi --prune` para remover com segurança apenas as imagens não referenciadas por nenhum container ou sandbox no nó.

## Conexões
- [[crictl-logs-exec-attach-port-forward-troubleshooting-local]] — Veja também: crictl: Coleta de Logs, Execução de Comandos e Port-Forward Direto no Nó (logs, exec e port-forward).
- [[crictl-stats-statsp-metricsp-metricdescs-substituicao-cadvisor]] — Veja também: crictl: Métricas e Estatísticas de Recursos CRI (stats, statsp, metricsp e metricdescs).

## Fontes
- [cri-tools Official Documentation — docs/crictl.md (CRI CLI Commands, /etc/crictl.yaml, runtime-endpoint, stats/statsp/metricsp, checkpoint & OpenTelemetry Tracing)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/docs/crictl.md) — Guia oficial completo do crictl detalhando todos os subcomandos de PodSandbox, containers, imagens e métricas CRI, configuração de /etc/crictl.yaml e flags de tracing/timeout; consultado em 2026-10-03.
- [kubernetes-sigs/cri-tools GitHub — README.md (Project Scope, Kubernetes Version Compatibility Matrix, crictl & critest Installation)](https://raw.githubusercontent.com/kubernetes-sigs/cri-tools/master/README.md) — README oficial do kubernetes-sigs/cri-tools explicando o escopo do crictl e do critest e a matriz de compatibilidade de versões minor com o Kubernetes; consultado em 2026-10-03.
- [Kubernetes SIG Node cri-tools — Official GitHub Repository](https://github.com/kubernetes-sigs/cri-tools) — Repositório oficial Apache-2.0 do cri-tools; consultado em 2026-10-03.
