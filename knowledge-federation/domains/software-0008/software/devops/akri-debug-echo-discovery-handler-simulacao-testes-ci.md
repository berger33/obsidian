---
id: software.devops.tranche17.001668
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/project-akri/akri/main/README.md", "https://docs.akri.sh/architecture/architecture-overview", "https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Akri: simulação de dispositivos folha intermitentes em CI/CD com o handler `debugEcho`

## Em uma frase
O Discovery Handler `debugEcho` do Akri permite simular a descoberta e o desaparecimento dinâmico de dispositivos folha locais ou compartilhados por meio de um simples arquivo em `/tmp/debug-echo-availability.txt` nos nós, sem exigir câmeras USB ou sensores físicos.

## Por que importa
Testar pipelines de borda em runners de CI (como clusters `kind`, `k3d` ou VMs de nuvem) seria impossível se toda validação do Akri dependesse de plugar e desplugar cabos USB físicos ou câmeras ONVIF reais.

## Como funciona
Ao instalar o Akri com `debugEcho.discovery.enabled=true` e `Configuration` apontando para `debugEcho`, o handler monitora o conteúdo do arquivo de disponibilidade no nó: escrever `ONLINE` no arquivo faz o Akri descobrir instantaneamente os dispositivos simulados, criar as `Instances`, os broker Pods e os `Services`; escrever `OFFLINE` simula a desconexão física e remove os brokers.

## Exemplo
```bash
helm install akri akri-helm-charts/akri \
  --set debugEcho.discovery.enabled=true \
  --set debugEcho.configuration.enabled=true \
  --set debugEcho.configuration.brokerPod.image.repository="nginx"
kubectl get akric,akrii,pods
```

## Limites e trade-offs
Por segurança, o handler `debugEcho` destina-se exclusivamente a ambientes de desenvolvimento, demonstração e testes automatizados, não devendo ser habilitado em clusters de produção.

## Como verificar
Altere o estado simulado do `debugEcho` no nó para offline e confirme que os objetos `akrii` e os broker Pods correspondentes são terminados automaticamente pelo Akri.

## Conexões
- [[akri-alta-disponibilidade-compartilhamento-dispositivos-rede-capacity]] — Veja também: Akri: compartilhamento multi-nó e alta disponibilidade de dispositivos de rede com `spec.capacity`.
- [[akri-broker-jobs-vs-pods-processamento-batch-dispositivos-borda]] — Veja também: Akri: execução de `brokerJobSpec` vs `brokerPodSpec` para tarefas batch disparadas por dispositivos.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://docs.akri.sh/architecture/architecture-overview) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
