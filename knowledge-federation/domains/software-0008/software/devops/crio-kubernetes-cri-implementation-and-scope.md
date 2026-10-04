---
id: software.devops.tranche04.000371
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CRI-O como implementação OCI dedicada da Container Runtime Interface (CRI) do Kubernetes

## Em uma frase
O CRI-O é uma implementação de código aberto da **Container Runtime Interface (CRI)** do Kubernetes baseada em padrões da Open Container Initiative (OCI), permitindo que o Kubelet inicie e gerencie diretamente contêineres compatíveis com OCI sem depender de daemons monolíticos genéricos. O README oficial define que o escopo do CRI-O é estritamente vinculado ao escopo da CRI do Kubelet: suportar múltiplos formatos de imagem (incluindo OCI e Docker), baixar imagens com verificação de confiança e assinatura, gerenciar camadas de imagem e sistemas de arquivos overlay, gerenciar o ciclo de vida dos processos de contêiner, prover monitoramento e logging exigidos pela CRI e aplicar isolamento de recursos.

## Por que importa
O README também define explicitamente **o que NÃO faz parte do escopo do CRI-O**: construir, assinar e enviar imagens para registros, ou fornecer uma CLI de usuário final com garantia de compatibilidade retroativa. Ao fazer única e exclusivamente o que o Kubelet precisa, o CRI-O minimiza a superfície de ataque e a complexidade operacional nos nós do cluster.

## Como funciona
Adote o CRI-O como runtime de contêiner dedicado em nós Kubernetes de produção e utilize ferramentas externas especializadas como **`crictl`** (`kubernetes-sigs/cri-tools`) ou **Podman** quando precisar inspecionar contêineres ou imagens manualmente no nó.

## Exemplo
Em um cluster Kubernetes corporativo, o Kubelet conversa via gRPC com o socket `unix:///var/run/crio/crio.sock` do CRI-O para criar pods, enquanto builds de imagem ocorrem separadamente em pipelines com BuildKit ou Buildah.

## Limites e trade-offs
Nunca dependa de binários auxiliares internos de teste do CRI-O como se fossem uma CLI geral de gerenciamento de contêineres; para depuração interativa da CRI no nó, utilize sempre `crictl`.

## Como verificar
Verifique nos nós do cluster com `kubectl get nodes -o wide` que a coluna `CONTAINER-RUNTIME` reporta `cri-o://1.x.y` e que o serviço `crio` está ativo no `systemd`.

## Conexões
- [[crio-kubernetes-version-matching-and-n-minus-2-skew-policy]] — Veja também: Matriz de compatibilidade CRI-O 1.x.y com o Kubernetes e política de version skew n-2.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
