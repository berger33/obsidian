---
id: software.devops.tranche04.000372
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

# Matriz de compatibilidade CRI-O 1.x.y com o Kubernetes e política de version skew n-2

## Em uma frase
A matriz de compatibilidade oficial do CRI-O estabelece que o projeto **segue exatamente os ciclos de release do Kubernetes em relação às suas versões minor (`1.x.y`)**: a branch `release-1.x` do CRI-O (`v1.x.y`) corresponde diretamente à branch `release-1.x` do Kubernetes (`v1.x.z`), e quando uma versão do Kubernetes atinge End of Life (EOL), a versão correspondente do CRI-O também entra em EOL. O CRI-O segue a política de desvio de versão (**version skew policy**) **`n-2`** do Kubernetes para graduação, depreciação ou remoção de funcionalidades, embora releases de patch (`1.x.z`) saiam conforme necessário e backports de funcionalidades independentes do Kubernetes possam ser avaliados caso a caso pela comunidade.

## Por que importa
O pareamento direto de versão minor (por exemplo, CRI-O `1.31.x` para Kubernetes `1.31.x`) elimina qualquer ambiguidade sobre qual versão do runtime de contêiner é homologada para determinada versão do Kubelet.

## Como funciona
Durante upgrades de versão minor do Kubernetes nos nós trabalhadores, atualize o pacote do CRI-O para a mesma série minor `1.x` do Kubelet, consultando sempre as notas de versão artesanais publicadas em `cri-o.github.io/cri-o`.

## Exemplo
Ao planejar o upgrade de um cluster Kubernetes da versão `1.30` para `1.31`, a automação de imagem de nó atualiza simultaneamente o Kubelet para `v1.31.z` e o CRI-O da série `1.30.y` para `1.31.y`.

## Limites e trade-offs
Não mantenha o CRI-O em uma versão minor mais de duas versões defasada (`n-2`) ou pertencente a uma série Kubernetes já em End of Life, pois a compatibilidade com a especificação CRI do Kubelet deixa de ser garantida.

## Como verificar
Compare a versão do Kubelet (`kubelet --version`) e a versão do CRI-O (`crio --version`) em cada nó trabalhador e confirme o alinhamento na mesma série minor `1.x`.

## Conexões
- [[crio-kubernetes-cri-implementation-and-scope]] — Veja também: CRI-O como implementação OCI dedicada da Container Runtime Interface (CRI) do Kubernetes.
- [[crio-oci-components-runc-container-libs-and-cni]] — Veja também: Arquitetura interna do CRI-O: runc, container-libs/image, container-libs/storage e CNI.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
