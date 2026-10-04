---
id: software.testes.tranche25.001894
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

# Instalação no Windows: binários .msi e Visual C++ redistributables

## Em uma frase
Na subseção Windows de Installing, o README informa que os binários do CBMC podem ser instalados pelos arquivos .msi disponíveis na página de releases do GitHub, observando que o executável depende dos Visual C++ redistributables (vcredist.x64.exe da Microsoft), que devem ser instalados antes de rodar o cbmc caso ainda não estejam presentes na máquina.

## Por que importa
Em imagens limpas de Windows Server ou runners de CI recém-provisionados, a ausência do runtime Visual C++ faz o binário falhar ao iniciar com erro de DLL ausente; documentar o pré-requisito vcredist.x64.exe evita falhas misteriosas de instalação.

## Como funciona
No Windows, verifique se os Visual C++ redistributables x64 estão instalados (baixando vcredist.x64.exe do suporte da Microsoft se necessário) e instale o pacote .msi correspondente à release desejada do CBMC.

## Exemplo
Em um pipeline Windows automatizado, o script de provisionamento garante a presença do vcredist.x64.exe antes de executar msiexec sobre o instalador do CBMC baixado das releases.

## Limites e trade-offs
O instalador .msi entrega os binários do CBMC, mas verificação de código C/C++ no Windows ainda requer que o ambiente possua os cabeçalhos e ferramentas de compilação apropriados para pré-processar o código alvo.

## Como verificar
Conferi a subseção Windows da seção Installing no README oficial.

## Conexões
- [[cbmc-releases-vs-develop-branch]] — Veja também: Política entre releases testadas para produção e a branch develop.
- [[cbmc-linux-install-abi-caveat]] — Veja também: Três caminhos de instalação no Linux e a ressalva de ABI da libc/libc++.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [Repositório oficial diffblue/cbmc](https://github.com/diffblue/cbmc) — Repositório oficial do CBMC e da suíte CProver no GitHub com releases, TOOLS_OVERVIEW.md, COMPILING.md, CODING_STANDARD.md e FEATURE_IDEAS.md.; consultado em 2026-10-03.
