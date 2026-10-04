---
id: software.seguranca.tranche13.001222
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Triagem Rápida vs. Engenharia Reversa Profunda no `capa`: Modos Padrão, Verboso (**`-v`**), Muito Verboso (**`-vv`**) e Exportação **`-j` JSON**

## Em uma frase
O `capa` oferece quatro níveis de detalhe de saída desenhados para diferentes momentos da análise de malware: **(1) Modo Padrão (`capa binario.exe`)** — ideal para triagem em 5 segundos: exibe a tabela executiva com hashes (`md5`, `sha1`, `sha256`), sistema operacional, arquitetura e três quadros lado a lado: **ATT&CK Tactic -> Technique**, **MBC Objective -> Behavior** e **Capability -> Namespace**!

## Por que importa
Quando você quer saber **em qual endereço de função (`0x401000`)** do binário cada capacidade foi encontrada para saltar direto para lá no desmontador, passe a flag **`-v` (*verbose*)**!

## Como funciona
E quando você quer ver **exatamente qual instrução de assembly, qual chamada de API (`call CreateRemoteThread`), qual constante numérica (`0x80000002 = HKEY_LOCAL_MACHINE`) ou qual string** disparou cada cláusula da regra dentro daquela função, passe a flag **`-vv` (*very verbose*)**! Para pipelines automatizados de triagem e ingestão no **capa Explorer Web**, passe **`-j` (`--json`)**!

## Exemplo
```bash
# Executar o capa em modo muito verboso (-vv) para inspecionar os enderecos exatos de funcoes, basic blocks e chamadas de API de cada capacidade
capa -vv ./amostras/suspicious_loader.exe
capa -j ./amostras/suspicious_loader.exe > ./relatorio_capa.json
```

## Limites e trade-offs
A saída do modo **`-vv`** funciona como um verdadeiro "mapa do tesouro" para o engenheiro reverso: em vez de perder horas analisando 800 funções de biblioteca estática dentro de um binário grande, o `-vv` aponta os 5 endereços exatos de funções (`function @ 0x140003A20`) onde estão a criptografia, a persistência e a comunicação C2!

## Como verificar
Use **`-q` (`--quiet`)** junto com `-j` quando estiver rodando o `capa` em lote dentro de scripts Python ou pipelines CI/CD de laboratório de malware.

## Conexões
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Veja também: Arquitetura do **Mandiant `capa` (`mandiant/capa`)**: Detecção Automatizada de Capacidades em Binários (**PE, ELF, .NET, Shellcode**) Mapeadas ao **MITRE ATT&CK** e **MBC**.
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Veja também: Anatomia das Regras YAML do **`capa-rules`**: Escopos Estáticos (**`file`, `function`, `basic block`, `instruction`**) e Operadores Lógicos (`and`, `or`, `count`, `optional`).
- [[capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web]] — Referência cruzada direta com capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
