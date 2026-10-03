---
id: software.devops.tranche04.000383
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

# Rastreamento de ciclo de vida de imagens com HCP Packer Registry e integração com Terraform

## Em uma frase
O README oficial apresenta o **HCP Packer** (`developer.hashicorp.com/packer/tutorials/hcp-get-started`) como um registro que armazena os **metadados das imagens construídas pelo Packer**, permitindo rastrear o ciclo de vida das imagens (como canais de versão, status de aprovação e revogação) através de múltiplas regiões e provedores de nuvem, e referenciá-las dinamicamente em configurações do **Terraform**. Nota: oHCP Packer armazena os metadados da imagem (como o ID da AMI gerada em cada região, data de criação e versão), enquanto o artefato pesado de disco permanece armazenado no próprio provedor de nuvem.

## Por que importa
Sem um registro central de metadados de imagens, equipes precisam copiar e colar IDs de AMIs manualmente em variáveis do Terraform a cada novo build do Packer ou usar filtros de busca por nome que podem selecionar acidentalmente uma imagem de teste ou uma versão vulnerável revogada.

## Como funciona
Integre seus templates `.pkr.hcl` ao registro de metadados (ou catálogo equivalente de artefatos) para publicar automaticamente os identificadores de imagem gerados em cada build e consuma o canal homologado diretamente via data source no Terraform.

## Exemplo
Após o `packer build` concluir a criação de uma nova AMI endurecida (hardened) na AWS, os metadados da build são registrados no canal `production`; na execução seguinte do Terraform, os grupos de nós buscam o ID atualizado da AMI daquele canal sem edição manual de código.

## Limites e trade-offs
Quando uma vulnerabilidade crítica é descoberta em uma imagem base antiga, revogue imediatamente a iteração correspondente no registro de metadados para impedir que novos `terraform apply` provisionem instâncias com a imagem comprometida.

## Como verificar
Verifique após o build que o identificador da imagem gerada por região e plataforma foi registrado corretamente nos metadados de saída do Packer para consumo pelo Terraform.

## Conexões
- [[packer-external-plugin-integrations-architecture]] — Veja também: Arquitetura de integrações via plugins externos no Packer (developer.hashicorp.com/packer/integrations).
- [[packer-local-docker-and-vagrant-box-workflows]] — Veja também: Desenvolvimento e teste local de templates Packer com imagens Docker e Vagrant boxes.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
