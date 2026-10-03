---
id: software.devops.tranche04.000389
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
fontes: ["https://raw.githubusercontent.com/hashicorp/packer/main/README.md", "https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md", "https://developer.hashicorp.com/packer/docs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Repositório unificado de documentação (hashicorp/web-unified-docs) e licença BUSL-1.1 no Packer

## Em uma frase
O README oficial do Packer destaca dois aspectos importantes de governança do repositório: o projeto é distribuído sob a licença **BUSL-1.1** (Business Source License 1.1, conforme badge e arquivo `LICENSE` na raiz), e toda a documentação oficial do Packer (`developer.hashicorp.com/packer/docs`) foi migrada para o repositório centralizado **`hashicorp/web-unified-docs`** (`github.com/hashicorp/web-unified-docs`), onde contribuições e correções de documentação devem ser abertas diretamente conforme as instruções da seção *Updating Documentation* do `CONTRIBUTING.md`.

## Por que importa
Equipes jurídicas e de engenharia de plataforma que auditam licenças de ferramentas de infraestrutura precisam registrar corretamente a licença BUSL-1.1 nas matrizes de conformidade, e contribuidores técnicos precisam saber onde abrir PRs de documentação para que não sejam enviados ao repositório errado.

## Como funciona
Ao consultar ou propor melhorias na documentação oficial do Packer, utilize o portal `developer.hashicorp.com/packer/docs` e direcione pull requests de documentação ao repositório `hashicorp/web-unified-docs`.

## Exemplo
Durante uma auditoria de ferramentas de automação no pipeline de imagens, o arquiteto registra a licença BUSL-1.1 do HashiCorp Packer no inventário de software e referencia a documentação canônica em `developer.hashicorp.com/packer/docs`.

## Limites e trade-offs
Não abra pull requests de correção de páginas do site de documentação diretamente no repositório de código `hashicorp/packer` sem verificar se o conteúdo reside em `hashicorp/web-unified-docs`.

## Como verificar
Verifique o arquivo `LICENSE` e as referências oficiais no `README.md` do repositório `hashicorp/packer` ao documentar a governança da ferramenta.

## Conexões
- [[packer-building-packer-from-source-and-go-requirements]] — Veja também: Compilação do Packer a partir do código-fonte com Go >= v1.20 e verificação de binários de PR.
- [[packer-immutable-infrastructure-pipeline-with-packer-and-iac]] — Veja também: Fluxo de infraestrutura imutável combinando Golden Images do Packer com provisionamento IaC.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
