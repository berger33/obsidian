---
id: software.devops.tranche04.000337
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
fontes: ["https://raw.githubusercontent.com/anchore/syft/main/README.md", "https://oss.anchore.com/docs/guides/sbom/getting-started/", "https://github.com/anchore/syft"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução 100% local sem telemetria externa e enriquecimento opcional com --enrich no Syft

## Em uma frase
O FAQ oficial do Getting Started do Syft esclarece dois pontos críticos de privacidade e operação em rede: (1) **o Syft executa inteiramente de forma local e não envia nenhum dado para serviços externos**, garantindo total confidencialidade sobre o código-fonte e a composição das imagens corporativas; e (2) por padrão, após o download da imagem de contêiner, a catalogação funciona **totalmente offline**, podendo opcionalmente baixar informações suplementares de fontes online apenas quando o usuário habilita explicitamente a flag `--enrich`.

## Por que importa
Equipes de segurança corporativa e ambientes regulados precisam de garantia formal de que a geração de SBOM de projetos proprietários não vaza nomes de pacotes internos, caminhos de arquivos ou metadados de build para servidores de terceiros.

## Como funciona
Execute o Syft em modo padrão (offline após o pull da imagem ou sobre diretórios/tarballs locais) em runners isolados de CI, habilitando `--enrich` apenas quando o pipeline tiver acesso controlado à internet e exigir metadados suplementares de repositórios públicos.

## Exemplo
Em um runner de build corporativo sem saída para a internet pública (conectado apenas ao registro OCI interno), o Syft analisa as imagens recém-construídas localmente com zero chamadas de rede externas e gera os SBOMs CycloneDX e SPDX.

## Limites e trade-offs
Ao habilitar `--enrich` em pipelines conectados, considere que a consulta a fontes online externas adiciona dependência de rede e latência ao tempo de geração do SBOM.

## Como verificar
Monitore as conexões de rede de uma execução padrão de `syft ./meu-diretorio` (sem `--enrich`) e confirme que nenhuma requisição externa é realizada pela ferramenta.

## Conexões
- [[syft-in-toto-signed-sbom-attestations]] — Veja também: Criação de atestações de SBOM assinadas segundo a especificação in-toto com Syft.
- [[syft-private-registry-authentication-and-scan-targets]] — Veja também: Autenticação em registros privados e variedade de alvos de scan suportados pelo Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
