---
id: software.devops.tranche01.000076
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://github.com/containerd/containerd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Estabilidade de API (`RELEASES.md`, `FEATURES.MD`) e autocompletar de shell para o cliente `ctr`

## Em uma frase
Na seção Features / Releases and API Stability, o README oficial remete a `docs/features.md` (visão detalhada dos conceitos centrais e funcionalidades) e a `RELEASES.md` (versionamento, estabilidade de componentes e matriz de suporte de plataformas em `RELEASES.md#platform-support`), além de documentar que desde o containerd 1.4 o autocompletar para `bash` e `zsh` do cliente `ctr` vem habilitado: basta rodar `source ./contrib/autocomplete/ctr` no `.bashrc` ou copiar `contrib/autocomplete/ctr` para `/etc/bash_completion.d/ctr` (e usar `zsh_autocomplete` no zsh).

## Por que importa
Administradores que depuram imagens, snapshots e tarefas diretamente nos nós via `ctr` ganham velocidade e evitam erros de digitação de subcomandos ao instalar o script de autocompletar em `/etc/bash_completion.d/ctr`, enquanto empacotadores de distribuições Linux encontram ali a instrução exata de como distribuir o recurso.

## Como funciona
Consulte `RELEASES.md` para verificar o ciclo de suporte e a matriz de arquiteturas antes de atualizar o daemon, e instale `contrib/autocomplete/ctr` em `/etc/bash_completion.d/ctr` (ou faça `source` no perfil do shell) nas imagens base dos nós.

## Exemplo
Além dos binários oficiais de 64 bits Intel/AMD e outras arquiteturas publicados na página de releases do GitHub, o README lembra que distribuições como o Ubuntu empacotam o containerd para múltiplas arquiteturas.

## Limites e trade-offs
Caso o pacote da sua distribuição não coloque o arquivo em um diretório carregado automaticamente pelo shell do usuário, oriente os operadores a fazer `source` manual do arquivo de autocompletar.

## Como verificar
Conferi a seção Features / Releases and API Stability e Enabling command auto-completion no README oficial.

## Conexões
- [[containerd-oci-distribution-registries-and-hosts-config]] — Veja também: Suporte a qualquer registry compatível com a OCI Distribution Specification e configuração em `docs/hosts.md`.
- [[containerd-cri-plugin-ga-kubernetes-integration]] — Veja também: O plugin nativo `cri` (GA): integração direta com a Container Runtime Interface do Kubernetes.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
