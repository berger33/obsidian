---
id: software.testes.tranche25.001893
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

# Política entre releases testadas para produção e a branch develop

## Em uma frase
A seção Versions do README distingue claramente dois canais: a latest release na página de releases do GitHub — onde "Releases are tested and for production use" — e a versão atual da branch develop obtida via git clone https://github.com/diffblue/cbmc.git, com o aviso expresso de que "Develop versions are not recommended for production use".

## Por que importa
Em pipelines de verificação formal corporativos, usar uma versão em desenvolvimento pode introduzir regressões ou mudanças de comportamento não validadas; o projeto reserva o selo de uso em produção exclusivamente para as releases fechadas.

## Como funciona
Em ambientes de produção e CI de projetos verificados, baixe sempre uma release oficial da página github.com/diffblue/cbmc/releases; reserve o clone da branch develop apenas para testar correções inéditas ou desenvolver contribuições para o próprio CBMC.

## Exemplo
Um job de CI que instala o pacote .deb ou .msi de uma release numerada segue a recomendação de produção do README, ao passo que compilar o topo da branch develop é voltado a contribuidores.

## Limites e trade-offs
A branch padrão de trabalho do repositório para pull requests é a develop (como detalhado na seção de contribuição), o que reforça a importância de não confundi-la com uma tag de release estável ao baixar binários.

## Como verificar
Conferi a seção Versions do README oficial do CBMC.

## Conexões
- [[cbmc-verified-properties-and-unwinding]] — Veja também: O que e como verifica: bounds, ponteiros, exceções, asserções e loop unwinding.
- [[cbmc-windows-msi-and-vcredist]] — Veja também: Instalação no Windows: binários .msi e Visual C++ redistributables.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
