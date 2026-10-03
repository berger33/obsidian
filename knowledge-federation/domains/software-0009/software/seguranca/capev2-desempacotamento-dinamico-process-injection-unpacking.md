---
id: software.seguranca.tranche06.000542
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

# CAPEv2 Sandbox: Desempacotamento Dinâmico Automático (*Passive* vs *Active Unpacking* `unpacker=2`) e Captura de Injeções

## Em uma frase
O CAPEv2 intercepta automaticamente técnicas de evasão e injeção de processos — incluindo *Shellcode Injection*, *DLL Injection*, *Process Hollowing*, *Process Doppelgänging* e alocação/descompressão de módulos PE em memória — para capturar e salvar os payloads desempacotados antes ou durante sua execução.

## Por que importa
Mesmo quando o binário submetido está ofuscado com um *crypter* inédito (0/70 no VirusTotal), no momento em que o *stub* do crypter decifra o executável real na RAM para transferi-lo a um processo filho ou saltar para o *Original Entry Point* (OEP), o CAPEv2 despeja a imagem PE limpa em disco.

## Como funciona
Além do modo padrão (*Passive Unpacking*, que captura payloads no momento da injeção, chamada de API ou término do processo), o CAPEv2 oferece o **Active Unpacking** (ativado pela opção **`unpacker=2`**): ele arma *guard pages* / breakpoints de escrita sobre regiões de memória recém-alocadas ou cuja proteção foi alterada (`VirtualAlloc` / `VirtualProtect`), capturando o payload no exato instante em que ele termina de ser escrito e antes de executar.

## Exemplo
```bash
# Submeter amostra suspeita via REST API v2 ativando o Active Unpacker (unpacker=2) e captura de dump de RAM
curl -sS -X POST "https://cape.soc.internal.corp/apiv2/tasks/create/file/" -H "Authorization: Token ${CAPE_API_TOKEN}" \
  -F "file=@/cases/samples/packed_loader.exe" \
  -F "options=unpacker=2,procdump=1" \
  -F "memory=1" | jq .
```

## Limites e trade-offs
Conforme documentado no README oficial do CAPEv2, a opção `unpacker=2` (*Active Unpacking*) vem desativada por padrão porque o overhead de exceções de página de memória pode alterar o tempo de execução (*timing*) de certos malwares; use o modo padrão primeiro e acione `unpacker=2` quando o packer exigir captura pré-execução.

## Como verificar
Consulte a seção `CAPE payloads` do relatório gerado e confirme que os arquivos PE desempacotados foram extraídos com seus respectivos hashes SHA-256 e classificações YARA.

## Conexões
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Veja também: CAPEv2 Sandbox: Arquitetura de Detonação de Malware, *API/Syscall Hooking* (`capemon`) e Debugger Furtivo Programável.
- [[capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox]] — Veja também: CAPEv2 Sandbox: Programação Dinâmica do Debugger via Assinaturas **YARA** (`meta: cape_options`) para Unpacking e Anti-Sandbox.
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Referência cruzada direta com volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
