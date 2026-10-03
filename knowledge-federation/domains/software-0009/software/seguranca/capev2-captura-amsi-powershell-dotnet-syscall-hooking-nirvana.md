---
id: software.seguranca.tranche06.000545
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md", "https://capev2.readthedocs.io/en/latest/usage/api.html", "https://github.com/CAPESandbox/CAPE-parsers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CAPEv2 Sandbox: Captura de Payloads **AMSI** (*Anti-Malware Scan Interface*), `.NET` / PowerShell / WSH e *Syscall Hooking* Anti-Evasão

## Em uma frase
No Windows 10 e Windows 11, o CAPEv2 instrumenta a **AMSI** (*Anti-Malware Scan Interface*) e utiliza técnicas avançadas de *syscall hooking* e *debugger-based direct/indirect syscall countermeasures* para derrotar malwares que tentam contornar ganchos em `ntdll.dll`.

## Por que importa
Scripts maliciosos em PowerShell, VBScript, JScript, macros Office VBA e assemblies `.NET` carregados em memória via `Assembly.Load(byte[])` passam obrigatoriamente pelo buffer da AMSI (`AmsiScanBuffer`) completamente desofuscados imediatamente antes de serem interpretados; o CAPEv2 intercepta e salva cada buffer AMSI como um artefato limpo.

## Como funciona
Para binários nativos C/C++/Rust/Go que usam *Unhooking* de `ntdll.dll`, *Hell's Gate* / *Halo's Gate* (*Direct Syscalls*) ou *Indirect Syscalls* (saltando para a instrução `syscall` dentro da `ntdll.dll` para fingir uma chamada legítima), o CAPEv2 combina instrumentação estilo Microsoft Nirvana e verificação da pilha de chamadas no debugger para capturar a telemetria mesmo sem depender do prólogo da função na `ntdll.dll`.

## Exemplo
```bash
# Submeter script PowerShell ofuscado forcando pacote ps1 e inspecao de buffers AMSI no Windows 11
curl -sS -X POST "https://cape.soc.internal.corp/apiv2/tasks/create/file/" -F "file=@/cases/samples/obfuscated_stage1.ps1" \
  -H "Authorization: Token ${CAPE_AMSI_TOKEN}" \
  -F "package=ps1" -F "platform=windows" -F "tags=win11_x64" | jq .
```

## Limites e trade-offs
Ao analisar instaladores `.msi`, scripts `.vbs`/`.js`/`.ps1` ou bibliotecas `.dll` exportando funções específicas (`options=function=DllRegisterServer`), especifique explicitamente o `package` adequado se a extensão original do arquivo tiver sido removida.

## Como verificar
Verifique nos artefatos extraídos da tarefa a presença dos buffers capturados pela AMSI contendo o código PowerShell/C# totalmente desofuscado.

## Conexões
- [[capev2-extracao-configuracao-malware-cape-parsers-maco-malduck]] — Veja também: CAPEv2 Sandbox: Extração Estática e Dinâmica de Configuração de Malware (`CAPE-parsers`, `extract_config`, `MaCo` e `MalDuck`).
- [[capev2-assinaturas-comportamentais-rede-suricata-mitre-attack]] — Veja também: CAPEv2 Sandbox: Classificação Tripla — Assinaturas Comportamentais Python, Inspeção PCAP com **Suricata** e Mapeamento MITRE ATT&CK.
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — Referência cruzada direta com capev2-desempacotamento-dinamico-process-injection-unpacking.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
