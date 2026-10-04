---
id: software.seguranca.tranche07.000633
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md", "https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md", "https://github.com/NationalSecurityAgency/ghidra/security/advisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ghidra: Automação em Linha de Comando e Pipelines CI/DFIR com **`analyzeHeadless`** (`-import`, `-preScript`, `-postScript` e `-readOnly`)

## Em uma frase
O utilitário **`support/analyzeHeadless`** executa todo o motor de importação, auto-análise e execução de scripts Java/Python do Ghidra em modo 100% *headless* (sem interface gráfica X11/Wayland), permitindo analisar centenas de amostras de malware ou pacotes de atualização de firmware em lote.

## Por que importa
Quando o CSIRT recebe 50 binários extraídos pelo CAPEv2 ou quando uma equipe de pesquisa de vulnerabilidades analisa todos os binários `.so`/ELF de uma imagem de firmware IoT, o `analyzeHeadless` importa a pasta inteira (`-import /cases/firmware/ -recursive`), roda os analisadores e executa scripts de extração de indicadores (`-postScript ExtractC2AndStrings.py`).

## Como funciona
A distinção entre **`-preScript`** e **`-postScript`** é fundamental: `-preScript` executa **antes** dos auto-analisadores do Ghidra (útil para configurar opções de análise, definir mapas de memória de firmware ou desativar analisadores lentos), enquanto `-postScript` executa **depois** que todas as funções, referências cruzadas e tabelas de tipos já foram reconstruídas.

## Exemplo
```bash
# Importar uma amostra de malware em modo headless, rodar auto-analise com timeout e executar pos-script Python
/opt/ghidra/support/analyzeHeadless /cases/ghidra-projects MalwareTriageProj \
  -import /cases/samples/unpacked_implant.bin \
  -analysisTimeoutPerFile 300 \
  -scriptPath /opt/secops/ghidra-scripts \
  -postScript ExportFunctionsAndCallsJson.py /cases/reports/implant_calls.json
```

## Limites e trade-offs
Se você estiver apenas executando um script de consulta sobre um projeto Ghidra já analisado e não quiser gravar alterações no banco do projeto, adicione a flag **`-readOnly`** (ou `-deleteProject` para projetos temporários descartáveis).

## Como verificar
Verifique a geração do arquivo `/cases/reports/implant_calls.json` e o código de saída `0` do `analyzeHeadless`.

## Conexões
- [[ghidra-representacao-intermediaria-pcode-analise-fluxo-dados-varnodes]] — Veja também: Ghidra: Análise de Fluxo de Dados (*Data-Flow / Taint Analysis*) sobre **P-Code** (`Varnode`, `PcodeOp`, *HighFunction* e *SSA Form*).
- [[ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao]] — Veja também: Ghidra: Desenvolvimento de Scripts em **Python 3 Nativo (`PyGhidra`)** e Uso da **`FlatProgramAPI`**.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — Referência cruzada direta com capev2-desempacotamento-dinamico-process-injection-unpacking.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
