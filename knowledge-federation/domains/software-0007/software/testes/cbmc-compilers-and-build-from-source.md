---
id: software.testes.tranche25.001898
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md", "https://github.com/diffblue/cbmc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Compilação a partir do código-fonte via COMPILING.md e qualidade monitorada

## Em uma frase
O README referencia o guia COMPILING.md para quem precisa compilar o CBMC a partir do código-fonte e exibe no topo os indicadores públicos de qualidade contínua do projeto: análise estática no Coverity Scan (scan.coverity.com/projects/diffblue-cbmc), cobertura de código no Codecov sobre a branch develop e pipelines de build AWS CodeBuild para Linux e Windows.

## Por que importa
Uma ferramenta de verificação formal precisa ela mesma passar por higiene rigorosa de engenharia; combinar cobertura medida no Codecov, varredura de defeitos no Coverity e builds automatizados em múltiplas plataformas dá transparência sobre o estado da branch develop.

## Como funciona
Quando binários pré-compilados não atenderem à sua plataforma ou você precisar alterar o código-fonte, siga as instruções de COMPILING.md e verifique os checks de CI ao abrir um pull request.

## Exemplo
Em uma distribuição Linux fora da família Debian/Ubuntu (como Fedora ou Arch) ou em arquiteturas não cobertas pelos pacotes .deb de release, o caminho suportado pelo README é seguir o COMPILING.md.

## Limites e trade-offs
Os badges de CodeBuild, Coverity e Codecov refletem o estado contínuo da branch develop no repositório oficial; para garantias de teste de release em produção, vale a regra da seção Versions de baixar releases fechadas.

## Como verificar
Conferi os badges e referências no topo e na subseção Linux do README oficial.

## Conexões
- [[cbmc-contributing-workflow-develop]] — Veja também: Fluxo de contribuição: branch a partir de develop e CODING_STANDARD.md.
- [[cbmc-license-4-clause-bsd]] — Veja também: Licenciamento sob 4-clause BSD license.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
