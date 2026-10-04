---
id: software.seguranca.tranche13.001225
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

# Análise Multi-Formato no `capa`: Executáveis **Windows PE**, **Linux ELF**, Assemblies **.NET (CIL)**, **Shellcode Bruto (`-f sc32`/`sc64`)** e Assinaturas **FLIRT (`-s`)**

## Em uma frase
Muitos analistas acham que o `capa` serve apenas para arquivos `.exe` nativos do Windows, deixando de aproveitá-lo na triagem de implantes Linux, binários .NET e shellcodes extraídos de memória.

## Por que importa
Na realidade, o motor moderno do `capa` analisa nativamente **cinco grandes famílias de artefatos**: **(1) Windows PE (`pe`)** em x86 (32-bit) e AMD64 (64-bit); **(2) Linux ELF (`elf`)** (essencial para triagem de backdoors Linux, implantes em containers e botnets IoT/cloud!); **(3) Assemblies .NET (`dotnet`)** compilados em *Common Intermediate Language (CIL)* (muito usados por infostealers, loaders e ferramentas de Red Team em C#); **(4) Shellcode bruto (`sc32` e `sc64`)** extraído de memória ou de exploits; e **(5) Relatórios de Sandbox**!

## Como funciona
Além disso, ao analisar binários compilados estaticamente em C/C++, o `capa` utiliza um diretório de **Assinaturas de Biblioteca FLIRT (`-s, --signatures`)** para reconhecer e **ignorar automaticamente milhares de funções internas de compiladores (MSVC runtime, glibc, OpenSSL estático)** — evitando que o analista perca tempo com capacidades internas da biblioteca padrão e focando 100% no código escrito pelo autor do malware!

## Exemplo
```bash
# Analisar um shellcode bruto de 64 bits extraido da memoria (-f sc64) e um binario ELF de Linux com o Mandiant capa
capa -f sc64 -vv ./dumps/beacon_payload_x64.bin
capa -f auto -v ./evidencias/linux_implant.elf
```

## Limites e trade-offs
Por que o `capa` precisa da flag explícita **`-f sc32`** ou **`-f sc64`** para analisar **Shellcode**? Porque um shellcode puro (*Position-Independent Code*) não possui cabeçalho `MZ`/`PE` nem cabeçalho `\x7fELF`; com `-f sc64`, o desmontador trata o arquivo binário desde o byte `0x00` como instruções de máquina x86_64 válidas!

## Como verificar
Em assemblies **.NET (`dotnet`)**, o `capa` inspeciona diretamente os metadados das tabelas CIL, chamadas de métodos da BCL (`System.Reflection.Assembly::Load`, `System.Security.Cryptography.Aes`) e P/Invoke (`DllImport`) sem precisar de desmontagem x86.

## Conexões
- [[capa-filtros-restricao-escopo-tags-functions-processes-otimizacao]] — Veja também: Acelerando o `capa` em Binários Complexos: Filtros por Tag/Namespace (**`-t`**), Restrição por Endereço de Função (**`--restrict-to-functions`**) e Cache **`.viv`**.
- [[capa-analise-dinamica-relatorios-sandbox-cape-drakvuf-vmray-processos]] — Veja também: Análise Dinâmica com o `capa`: Extraindo Capacidades de Relatórios de **Sandboxes (`CAPE`, `DRAKVUF`, `VMRay`)** e Filtrando por **PID (`--restrict-to-processes`)**.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.
- [[floss-extracao-strings-go-rust-utf8-estruturas-slice-sem-null-byte]] — Referência cruzada direta com floss-extracao-strings-go-rust-utf8-estruturas-slice-sem-null-byte.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
