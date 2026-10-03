---
id: software.devops.tranche06.000599
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

# Desenvolvimento local (nomad agent -dev), manifestos Terraform de referência e arquitetura de produção

## Em uma frase
A seção *Quick Start* do README oficial separa claramente o fluxo de **Testing (desenvolvimento/avaliação)** do fluxo de **Production (produção)**: para testes rápidos na estação de trabalho, segue-se o tutorial *Getting Started* (`developer.hashicorp.com/nomad/tutorials/get-started`, iniciando um cluster local de nó único com `nomad agent -dev`, que atua simultaneamente como `server` e `client`) ou utilizam-se os **manifestos Terraform oficiais incluídos no próprio diretório `terraform/` do repositório** para subir um cluster Nomad de desenvolvimento em nuvem pública. Já para **produção**, o README exige seguir a **Production Reference Architecture** (`developer.hashicorp.com/nomad/docs/deploy/production/reference-architecture`).

## Por que importa
Subir um cluster completo no laptop em 1 segundo com um único comando `sudo nomad agent -dev` (ou `nomad agent -dev-connect` para testar Service Mesh em Linux) permite desenvolver e validar arquivos `.nomad.hcl` localmente com rapidez incomparável; contudo, os manifestos do diretório `terraform/` e o modo `-dev` são explicitamente voltados para uso não produtivo.

## Como funciona
Use `nomad agent -dev` no laptop para validar especificações de jobs e os manifestos de `terraform/` para laboratórios rápidos em nuvem, mas aplique sempre a *Production Reference Architecture* (múltiplos servidores dedicados, TLS mTLS RPC, criptografia gossip, ACLs habilitadas e telemetria) ao provisionar clusters de produção.

## Exemplo
Um desenvolvedor testa seu novo arquivo `api.nomad.hcl` localmente rodando `nomad agent -dev` em um terminal e `nomad job run api.nomad.hcl` em outro, visualizando a alocação na Nomad UI local em `http://localhost:4646` antes de abrir o PR para o cluster produtivo.

## Limites e trade-offs
Nunca utilize os módulos simplificados de laboratório do diretório `terraform/` do repositório diretamente como infraestrutura final de produção sem antes aplicar o hardening de rede, IAM, TLS e ACLs descrito na *Production Reference Architecture*.

## Como verificar
Inicie um agente de teste ou inspecione um cluster ativo com `nomad agent-info` para verificar o status dos subsistemas `server`, `client` e `raft`.

## Conexões
- [[nomad-nomad-cli-api-and-plugin-ecosystem-operations]] — Veja também: Operação via Nomad CLI (developer.hashicorp.com/nomad/commands), HTTP API e ecossistema de Plugins.
- [[nomad-busl-1-1-license-nomad-enterprise-and-public-roadmap-governance]] — Veja também: Licenciamento BUSL-1.1, Nomad Enterprise, repositório web-unified-docs e ressalvas do Public Roadmap.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
