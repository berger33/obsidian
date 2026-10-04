---
id: software.devops.tranche04.000388
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

# Compilação do Packer a partir do código-fonte com Go >= v1.20 e verificação de binários de PR

## Em uma frase
O guia oficial `.github/CONTRIBUTING.md` detalha os requisitos para compilar e testar o Packer a partir do código-fonte: o projeto exige **Go >= v1.20** (lançando sempre a partir da versão mais recente do Golang), clonado em `$GOPATH/src/github.com/hashicorp/packer`, onde o comando `make` (ou `go build -o bin/packer .` em sistemas POSIX, e `go build -o bin/packer.exe` com MinGW Tools `mingw32-make` no Windows) executa os testes e gera o binário `$GOPATH/src/github.com/hashicorp/packer/bin/packer` para validação com `packer build template.pkr.hcl` e formatação obrigatória via `go fmt`. O guia também informa como baixar binários experimentais gerados pela CI (`store_artifacts`) em Pull Requests para testar correções em ambientes especializados.

## Por que importa
Quando uma equipe enfrenta um bug específico de ambiente e precisa testar um patch em revisão ou desenvolver uma correção para o core do Packer, seguir a estrutura exata do `GOPATH` e os alvos do `Makefile` evita erros de resolução de pacotes Go descritos na documentação.

## Como funciona
Ao compilar o Packer do código-fonte, clone o repositório no caminho canônico `$(go env GOPATH)/src/github.com/hashicorp/packer` (pois `go build` pode quebrar se um fork for clonado diretamente fora do caminho de pacotes esperado), execute `make` e valide o binário gerado em `./bin/packer`.

## Exemplo
Um engenheiro que desenvolve um patch para o Packer compila o projeto com `make`, testa `./bin/packer build template.pkr.hcl`, executa `go fmt` e valida os artefatos gerados pela CI antes da revisão final do time mantenedor.

## Limites e trade-offs
Observe o alerta explícito do `CONTRIBUTING.md`: o Go infere nomes de pacotes a partir dos caminhos de arquivo no `GOPATH`, portanto mantenha o diretório de trabalho em `$GOPATH/src/github.com/hashicorp/packer` e adicione seu fork como remote para fazer `git push`.

## Como verificar
Após compilar com `go build -o bin/packer .`, execute `./bin/packer version` para confirmar a execução limpa do binário compilado localmente.

## Conexões
- [[packer-hcl2-templates-and-reproducible-test-cases]] — Veja também: Templates HCL2 (template.pkr.hcl) e criação de casos de teste mínimos reproduzíveis no Packer.
- [[packer-unified-documentation-and-license-governance]] — Veja também: Repositório unificado de documentação (hashicorp/web-unified-docs) e licença BUSL-1.1 no Packer.

## Fontes
- [HashiCorp Packer GitHub — README.md (Multi-Platform Parallel Image Building, Plugins & HCP Packer)](https://raw.githubusercontent.com/hashicorp/packer/main/README.md) — README oficial do HashiCorp Packer descrevendo construção paralela de imagens de máquina idênticas para múltiplas plataformas a partir de uma única configuração, integrações via plugins externos, conversão para Vagrant boxes, HCP Packer registry de metadados e política para plugins não mantidos.; consultado em 2026-10-03.
- [HashiCorp Packer GitHub — .github/CONTRIBUTING.md (PACKER_LOG, template.pkr.hcl & Go Dev Workflow)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md) — Guia oficial de contribuição e diagnóstico do Packer detalhando execução com PACKER_LOG=1 packer build template.pkr.hcl, sanitização de chaves sensíveis, requisito de Go >= v1.20 e ciclo de vida de issues e pull requests.; consultado em 2026-10-03.
- [HashiCorp Developer — Official Packer Documentation](https://developer.hashicorp.com/packer/docs) — Portal oficial de documentação do HashiCorp Packer e catálogo de integrações em developer.hashicorp.com/packer/integrations.; consultado em 2026-10-03.
