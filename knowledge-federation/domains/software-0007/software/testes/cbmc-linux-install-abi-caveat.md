---
id: software.testes.tranche25.001895
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

# Três caminhos de instalação no Linux e a ressalva de ABI da libc/libc++

## Em uma frase
Para ambientes Linux, o README enumera três opções: (1) instalar pelos repositórios da distribuição, com a desvantagem de possivelmente trazer uma versão antiga conforme a política de pacotes da distro; (2) baixar o pacote .deb gerado a cada release e rodar apt install cbmc-x.y.deb como root; ou (3) compilar do código-fonte seguindo COMPILING.md — acrescentando uma nota crítica na opção 2 sobre compatibilidade de ABI de libc/libc++ e nomes de dependências.

## Por que importa
Pacotes .deb binários compilados para Ubuntu 24.04 não têm a mesma ABI de libc++ nem os mesmos nomes de pacotes de dependência de um Debian antigo ou Ubuntu 22.04; escolher o .deb errado para a versão do sistema operacional quebra a instalação no apt.

## Como funciona
Se precisar de versão recente no Linux sem compilar do zero, baixe na página de releases o arquivo .deb construído especificamente para a versão do seu sistema operacional e instale-o com apt install cbmc-x.y.deb; se a sua distro não tiver .deb compatível, siga o COMPILING.md.

## Exemplo
Ao atualizar o runner de CI de uma versão LTS do Ubuntu para outra, troque também o artefato cbmc-x.y.deb baixado na release para o pacote correspondente à nova versão do SO.

## Limites e trade-offs
Usar o pacote padrão da distribuição (opção 1) é simples, mas pode deixar o time sem suporte a recursos novos de C17/C23 ou correções recentes do solver.

## Como verificar
Conferi a subseção Linux da seção Installing no README oficial.

## Conexões
- [[cbmc-windows-msi-and-vcredist]] — Veja também: Instalação no Windows: binários .msi e Visual C++ redistributables.
- [[cbmc-macos-homebrew-pin-and-tap]] — Veja também: Instalação no macOS com Homebrew: upgrade automático, brew pin e tap histórico.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
