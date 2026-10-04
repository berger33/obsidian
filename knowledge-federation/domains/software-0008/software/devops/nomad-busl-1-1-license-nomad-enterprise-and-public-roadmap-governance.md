---
id: software.devops.tranche06.000600
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/nomad/main/README.md", "https://developer.hashicorp.com/nomad/docs", "https://github.com/hashicorp/nomad"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Licenciamento BUSL-1.1, Nomad Enterprise, repositório web-unified-docs e ressalvas do Public Roadmap

## Em uma frase
O README oficial documenta quatro aspectos importantes de governança do projeto Nomad: (1) o código é distribuído sob a licença **`BUSL-1.1`** (`LICENSE`); (2) existe a versão comercial **Nomad Enterprise** (`developer.hashicorp.com/nomad/docs/enterprise`, com recursos adicionais como *Multiregion Federation* avançada, *Resource Quotas*, *Sentinel Policies* e *Dynamic Application Sizing*); (3) a documentação do produto é armazenada no repositório unificado **`hashicorp/web-unified-docs`** e o guia de desenvolvedores fica no diretório `contributing/`; e (4) o **Public Roadmap** (`github.com/orgs/hashicorp/projects/202/views/1`) mostra as funcionalidades previstas para as próximas uma ou duas releases, trazendo a ressalva expressa de que datas e itens estão sujeitos a mudanças e **não devem ser tomados como compromissos formais (do not take any of these items as commitments)**, especialmente além da próxima major release.

## Por que importa
Equipes de arquitetura que planejam migrações ou dependem de funcionalidades futuras precisam conhecer tanto os termos da licença `BUSL-1.1` e a fronteira entre a edição comunitária e o Nomad Enterprise quanto a política oficial da HashiCorp sobre o roadmap público.

## Como funciona
Registre a licença `BUSL-1.1` no inventário de governança ao adotar versões atuais do Nomad, baseie suas decisões arquiteturais de produção nos recursos já lançados e documentados em `developer.hashicorp.com/nomad/docs` (e não em itens futuros do roadmap) e consulte `contributing/` ao colaborar com o código-fonte.

## Exemplo
Durante o planejamento anual de plataforma, a equipe consulta o Public Roadmap do Nomad para acompanhar a evolução de suporte a dispositivos e CSI, mas projeta os contratos de produção exclusivamente sobre as funcionalidades já estáveis na versão atual.

## Limites e trade-offs
Ao abrir pull requests de melhoria na documentação oficial do Nomad, lembre-se da nota no README: a documentação do produto reside no repositório `github.com/hashicorp/web-unified-docs/` (enquanto a documentação interna para desenvolvedores do core fica em `contributing/` no próprio repositório `hashicorp/nomad`).

## Como verificar
Verifique a versão e edição do binário (`nomad version`) e consulte as notas de release oficiais antes de realizar upgrades dos servidores e clientes Nomad.

## Conexões
- [[nomad-local-dev-agent-and-terraform-cloud-reference-manifests]] — Veja também: Desenvolvimento local (nomad agent -dev), manifestos Terraform de referência e arquitetura de produção.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
