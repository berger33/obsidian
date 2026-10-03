---
id: software.devops.tranche04.000381
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

# Packer para construção paralela de imagens de máquina idênticas a partir de configuração única

## Em uma frase
O HashiCorp Packer é uma ferramenta leve, multiplataforma e de alto desempenho para construir **imagens de máquina idênticas para múltiplas plataformas em paralelo a partir de um único arquivo de configuração fonte** (como `template.pkr.hcl`). Conforme documentado no README oficial, o Packer roda nos principais sistemas operacionais e permite gerar simultaneamente imagens para provedores de nuvem pública (como AWS AMIs), hipervisores de virtualização, contêineres Docker locais e boxes do **Vagrant** (`vagrantup.com`) a partir da mesma especificação de provisionamento.

## Por que importa
Configurar servidores manualmente após o boot ou rodar longos scripts de instalação de pacotes a cada auto-scaling atrasa a inicialização de novas instâncias e cria deriva de configuração (configuration drift) entre ambientes de desenvolvimento, homologação e produção. O padrão de **infraestrutura imutável** com Golden Images geradas pelo Packer elimina essa deriva.

## Como funciona
Defina um template HCL (`.pkr.hcl`) único que declare múltiplos builders/sources (por exemplo, uma imagem Docker ou Vagrant para teste local e uma AMI AWS para produção) aplicando exatamente os mesmos provisionadores (scripts shell, Ansible, arquivos de configuração).

## Exemplo
Para garantir paridade entre o ambiente local dos desenvolvedores e a nuvem de produção, um único comando `packer build template.pkr.hcl` constrói em paralelo uma AMI na AWS e uma imagem local Docker/Vagrant com exatamente os mesmos pacotes Linux e binários pré-instalados.

## Limites e trade-offs
Evite manter scripts de provisionamento separados e duplicados para cada nuvem ou ambiente virtualizado; centralize a lógica de configuração no template único do Packer e varie apenas os blocos de `source` de cada plataforma.

## Como verificar
Execute `packer validate template.pkr.hcl` seguido de `packer build template.pkr.hcl` e confirme a geração paralela bem-sucedida dos artefatos de imagem em todas as plataformas declaradas.

## Conexões
- [[packer-external-plugin-integrations-architecture]] — Veja também: Arquitetura de integrações via plugins externos no Packer (developer.hashicorp.com/packer/integrations).

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
