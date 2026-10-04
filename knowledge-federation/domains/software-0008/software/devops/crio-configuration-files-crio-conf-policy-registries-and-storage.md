---
id: software.devops.tranche04.000374
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

# Arquivos de configuração do CRI-O: crio.conf, policy.json, registries.conf e storage.conf

## Em uma frase
A tabela oficial de configuração do CRI-O destaca quatro arquivos principais de administração no host Linux: **`crio.conf(5)`** (por padrão `/etc/crio/crio.conf` e fragmentos drop-in), que controla o daemon `crio(8)`; **`policy.json(5)`** (`containers-policy.json`), que define a política de verificação de assinaturas criptográficas das imagens; **`registries.conf(5)`** (`containers-registries.conf`), que configura registros de busca, espelhos (mirrors), bloqueios e redirecionamentos para ambientes desconectados; e **`storage.conf(5)`** (`containers-storage.conf`), que parametriza o driver de armazenamento e diretórios de camadas.

## Por que importa
Separar a configuração do daemon (`crio.conf`), a política de confiança de assinatura (`policy.json`), o roteamento de registros/mirrors (`registries.conf`) e o armazenamento em disco (`storage.conf`) permite aplicar governança de segurança e espelhamento de imagens no nível do nó de forma transparente para os manifestos dos pods.

## Como funciona
Utilize `registries.conf` para redirecionar pulls de registros externos para um espelho OCI interno ou cache local sem precisar reescrever a URL da imagem em centenas de manifestos YAML do cluster, e endureça `policy.json` para exigir assinaturas válidas de registros corporativos.

## Exemplo
Em um cluster corporativo air-gapped, os administradores configuram `registries.conf` nos nós CRI-O para mapear `quay.io` e `ghcr.io` para o registro mirror interno, permitindo que Helm charts de terceiros subam sem alterar os nomes das imagens.

## Limites e trade-offs
Ao editar configurações do CRI-O, prefira arquivos drop-in em `/etc/crio/crio.conf.d/` em vez de sobrescrever diretamente o arquivo principal do pacote, evitando conflitos durante atualizações de pacotes RPM/DEB.

## Como verificar
Execute `sudo crio status config` para inspecionar a configuração TOML efetiva completa carregada pelo daemon `crio` em execução.

## Conexões
- [[crio-oci-components-runc-container-libs-and-cni]] — Veja também: Arquitetura interna do CRI-O: runc, container-libs/image, container-libs/storage e CNI.
- [[crio-http-status-api-and-crio-status-cli]] — Veja também: Inspeção de runtime com crio status e API HTTP sobre socket Unix /var/run/crio/crio.sock.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
